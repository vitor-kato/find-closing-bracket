import React, { Component } from 'react';
import BracketService from './BracketService';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const bracketService = new BracketService();

class BracketCreateUpdate extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount () {
        const { match: { params } } = this.props;
        if (params && params.id) {
            bracketService.getBracket(params.id).then((c) => {
                this.refs.string.value = c.string;
                this.refs.index.value = c.index;
            })
        }
    }

    handleCreate () {
        bracketService.createBracket(
            {
                "string": this.refs.string.value,
                "index": parseInt(this.refs.index.value),
            }
        ).then((result) => {
            console.log(result);
            this.props.history.push('/bracket')
            alert("FindBracket created!");
        }).catch((error) => {
            console.log(error.response);
            alert('There was an error! Please re-check your URL.');
        });
    }
    handleUpdate (id) {
        bracketService.updateBracket(
            {
                "id": id,
                "string": this.refs.string.value,
                "index": parseInt(this.refs.index.value),
            }
        ).then((result) => {
            console.log(result);
            this.props.history.push('/bracket')
            alert("FindBracket updated!");
        }).catch((error) => {
            console.log(error);
            alert('There was an error! Please re-check your URL.');
        });
    }
    handleSubmit (event) {
        const { match: { params } } = this.props;

        if (params && params.id) {
            this.handleUpdate(params.id);
        }
        else {
            this.handleCreate();
        }

        event.preventDefault();
    }

    render () {
        return (
            <div
                className="create--bracket"
                style={{
                    position: "absolute",
                    left: "50%",
                    top: "50%",
                    width: "50%",
                    transform: "translate(-50%, -50%)",
                }}
            >
                <Form onSubmit={this.handleSubmit}>
                    <h2
                        style={{ textAlign: "justify" }}>
                        Enter an expression with brackets and a index to find out where is the matching closing bracket
                    </h2>
                    <br />
                    <Form.Group controlId="formPostString">
                        <Form.Label>Expression With Brackets</Form.Label>
                        <Form.Control size="lg" ref='string' placeholder="E.g. [ABC[23]][89]" />
                    </Form.Group>
                    <Form.Group controlId="formPostIndex">
                        <Form.Label>Open Bracket Index</Form.Label>
                        <Form.Control type="number" size="lg" ref='index' placeholder="E.g. 0" />
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </div>
        );
    }
}

export default BracketCreateUpdate;