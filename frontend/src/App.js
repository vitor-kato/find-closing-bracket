import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route } from 'react-router-dom'
import BracketList from './BracketList'
import BracketCreateUpdate from './BracketCreateUpdate'
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

import "./App.css";

const BaseLayout = () => (
  <Container fluid
    style={{ padding: "0" }}
  >
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Navbar.Brand href="/">FIND CLOSING BRACKET APP</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="/">NEW BRACKET</Nav.Link>
          <Nav.Link href="/bracket">BRACKETS LIST</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
    <Container>
      <div className="content">
        <Route path="/bracket" exact component={BracketList} />
        <Route path="/bracket/:id" component={BracketCreateUpdate} />
        <Route path="/" exact component={BracketCreateUpdate} />
      </div>
    </Container>
  </Container>
)


class App extends Component {
  render () {
    return (
      <BrowserRouter>
        <BaseLayout />
      </BrowserRouter>
    );
  }
}

export default App;
