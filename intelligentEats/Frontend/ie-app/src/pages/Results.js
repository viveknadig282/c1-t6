import React, {useState, Component} from 'react';
import BarcodeGenerator from '../Components/Scanner/BarcodeGenerator';
import BarcodeScanner from '../Components/Scanner/BarcodeScanner';
import Itemlist from '../Components/Item/Itemlist';
import Receipt from '../Components/Receipt/Receipt';
import Search from '../Components/Search/Search';
import './Results.css';
import {Col, Row, Container} from 'react-bootstrap';


class Results extends Component {
  constructor(props) {
      super(props);
      this.state = {
        upc: '',
        itemList: [],
        healthScore: 0
      };
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({upc: event.target.value});
    }
  
    
    handleSubmit(event) {
      event.preventDefault();
      
      fetch(`http://127.0.0.1:8000/upc/${this.state.upc}`,{
        method: 'GET',
      })
      .then(async (response) => await response.json())
      .then(response => {

        this.setState({itemList: response});

        let scoreList = [];
        response.map(item => {
          scoreList.push(item.score);
        });

        let sum = (scoreList.reduce((previousValue, currentValue) => previousValue + currentValue));

        this.setState({healthScore: Math.round((sum/scoreList.length) * 100) / 100});
        

        console.log(this.state.itemList);
        console.log(this.state.healthScore);

        
      })
      .catch(error => {
        console.log(error);
      });
      console.log(this.state.upc);
    }

    render(){
        return(
            <>
            <Container className="hero-img" fluid>
                <div className="display-1 p-0 m-0 score-text"> 
                    We rank your item with a health score of  
                    <p className="healthScore m-0 p-0">{this.state.healthScore}</p>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        <input className="search-input p-4" placeholder="Enter A UPC Code..." value={this.state.upc} onChange={this.handleChange} />
                    </label>
                </form>
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
    
}
export default Results;
