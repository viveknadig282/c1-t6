import React from 'react';
import BarcodeGenerator from '../Components/Scanner/BarcodeGenerator';
import BarcodeScanner from '../Components/Scanner/BarcodeScanner';
import Itemlist from '../Components/Item/Itemlist';
import Receipt from '../Components/Receipt/Receipt';
import Search from '../Components/Search/Search';
import './Results.css';
import {Col, Row, Container} from 'react-bootstrap';


function Results(){

    return(
        <>
        <Container className="hero-img" fluid>
            <div className="display-1 score-text"> We rank your item with a health score of -0.000</div>
        </Container>
        <div className="mt-5">
            <h1>Find Out Why</h1>
            <Row className="m-5">
                <Col>
                    <h1>Items</h1>
                    <Itemlist/>
                </Col>
                <Col>
                    <Receipt/>
                </Col>
            </Row>
        </div>
        </>
        
    )
}
export default Results;
