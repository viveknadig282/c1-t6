import React, {useState} from 'react';
import BarcodeGenerator from '../Components/Scanner/BarcodeGenerator';
import BarcodeScanner from '../Components/Scanner/BarcodeScanner';
import Itemlist from '../Components/Item/Itemlist';
import Receipt from '../Components/Receipt/Receipt';
import Search from '../Components/Search/Search';
import './Results.css';
import {Col, Row, Container} from 'react-bootstrap';


function Results(){

    const [healthScore, setHealthScore] = useState(0);

    return(
        <>
        <Container className="hero-img" fluid>
            <div className="display-1 p-0 m-0 score-text"> 
                We rank your item with a health score of  
                <p className="healthScore m-0 p-0"> {healthScore}</p>
            </div>
            <Search/>
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
