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
        onSubmit: false,
        itemList: [],
        item_image: '',
        item_desc: '',
        healthScore: 0
      };
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({upc: event.target.value});
      this.setState({onSubmit: false});
    }
  
    
    handleSubmit(event) {
      event.preventDefault();

      this.setState({onSubmit: true});
      
      fetch(`http://127.0.0.1:8000/upc/${this.state.upc}`,{
        method: 'GET',
      })
      .then((response) => response.json())
      .then(response => {

        this.setState({itemList: response.ingredient_scores});

        let scoreList = [];
        this.state.itemList.map(item => {
          scoreList.push(item.score);
        });

        let sum = (scoreList.reduce((previousValue, currentValue) => previousValue + currentValue));

        this.setState({healthScore: Math.round((sum/scoreList.length) * 100) / 100});
        this.setState({item_desc: response.description});
        this.setState({item_image: response.image_url});


        console.log(this.state.item_desc);
        console.log(this.state.item_image);

        
      })
      .catch(error => {
        console.log(error);
        alert("try again");
      });
      console.log(this.state.upc);
    }

    render(){
        return(
            <>
            <Container className="hero-img" fluid>
                <div className="display-1 p-0 m-0 score-text"> 
                    We rank your item with a health score of  
                    <p className="healthScore m-0 p-0"> {this.state.healthScore}</p>
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
                        <Itemlist itemList={(this.state.onSubmit) ? this.state.itemList : ''}/>
                    </Col>
                    <Col>
                        <Receipt upc={(this.state.onSubmit) ? this.state.upc : ''} image={this.state.item_image} description={this.state.item_desc}/>
                    </Col>
                </Row>
            </div>
            {/* <BarcodeScanner/> */}
            </>
            
        )
    }
    
}
export default Results;
