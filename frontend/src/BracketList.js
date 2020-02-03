import React, {
    Component
} from "react";
import BracketService from "./BracketService";
import { Link } from 'react-router-dom'
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';


const bracketService = new BracketService();

class bracketList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bracket: [],
            nextPageURL: "",
            pages: "",
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }
    componentDidMount () {
        let self = this;
        bracketService.getBrackets().then(function (result) {
            console.log('result', result);
            self.setState({
                bracket: result.data,
                nextPageURL: result.nextlink,
                pages: result.numpages
            });
        });
    }
    handleDelete (e, id) {
        let self = this;
        bracketService
            .deleteBracket({
                id: id
            })
            .then(() => {
                let newArr = self.state.bracket.filter(function (obj) {
                    return obj.id !== id;
                });

                self.setState({
                    bracket: newArr
                });
            });
    }
    nextPage () {
        let self = this;
        console.log(this.state.nextPageURL);
        bracketService.getBracketByURL(this.state.nextPageURL).then(result => {
            self.setState({
                bracket: result.data,
                nextPageURL: result.nextlink,
            });
            console.log(this.state);

        });
    }
    render () {

        return (
            <div className="bracket--list">
                <Table responsive>
                    <thead key="thead">
                        <tr>
                            <th>STRING</th>
                            <th>OPEN BRACKET INDEX</th>
                            <th>CLOSING BRACKET INDEX</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.bracket.map(c =>
                            <tr key={c.id}>
                                <td>{c.string}</td>
                                <td style={{ whiteSpace: "pre-line" }}>{c.index}</td>
                                <td style={{ whiteSpace: "pre-line" }}>{c.closing_position_info}</td>
                                <td>
                                    <button type="button" className="btn btn-outline-danger" onClick={(e) => this.handleDelete(e, c.id)}>Delete</button>
                                    <br /><br />
                                    <Link to={"/bracket/" + c.id}>
                                        <button type="button" className="btn btn-outline-secondary">Update</button>
                                    </Link>
                                </td>
                            </tr>)}
                    </tbody>
                </Table>
                <Button
                    onClick={this.nextPage}
                    variant="primary"
                    type="submit"
                    disabled={this.state.pages > 1 ? false : true}
                >
                    Next page
                </Button>
            </div>
        );
    }
}

export default bracketList;