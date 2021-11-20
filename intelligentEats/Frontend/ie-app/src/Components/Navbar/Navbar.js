
import React from "react";
import {Navbar, Container, Nav} from 'react-bootstrap';
import './Navbar.css';
function TopNavbar(){
    return(
        <>
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="#home">Intelligent Eats</Navbar.Brand>
                <Nav className="me-auto">
                {/* <Nav.Link href="#features">Features</Nav.Link>
                <Nav.Link href="#pricing">Pricing</Nav.Link> */}
                </Nav>
                </Container>
            </Navbar>
        </>
    );
}

export default TopNavbar
;