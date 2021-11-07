import React from 'react';
import BarcodeGenerator from '../Components/Scanner/BarcodeGenerator';
import BarcodeScanner from '../Components/Scanner/BarcodeScanner';
import Itemlist from '../Components/Item/Itemlist';
import Receipt from '../Components/Receipt/Receipt';
import {Col, Row} from 'react-bootstrap';


function Results(){

    return(
        <div>
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
    )
}
export default Results;
