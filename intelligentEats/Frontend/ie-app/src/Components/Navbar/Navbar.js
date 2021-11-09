
import React from "react";
import {Navbar, Container, Nav} from 'react-bootstrap';
function ieNavbar(){
    return(
        <>
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="#home">Intelligent Eats</Navbar.Brand>
                <Nav className="me-auto">
                <Nav.Link href="#">How It Works</Nav.Link>
                {/* <Nav.Link href="#features">Features</Nav.Link>
                <Nav.Link href="#pricing">Pricing</Nav.Link> */}
                </Nav>
                </Container>
            </Navbar>
        </>
    );
}

export default ieNavbar;