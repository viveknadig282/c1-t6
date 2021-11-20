import React from 'react';
import TopNavbar from '../Components/Navbar/Navbar';
import './Home.css';
import heroImg from '../assets/grocery_hero.png';
import {Navbar, Container, Nav, Row, Col, Button} from 'react-bootstrap';
import Search from '../Components/Search/Search';
import barcode from '../assets/barcode.png';
import links from '../assets/links.png';
import score from '../assets/score.png';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";


function Home(){
    return(
        <div>
            {/* <TopNavbar/> */}
            <Container fluid className="p-0 m-0 hero-container">
                <img src={heroImg} alt="grocery store" className="hero_img"/>
                <div className="centered">
                    <h1>Find out how healthy your foods are</h1>
                    <div className="search-div">
                        <Search/>
                    </div>
                </div>
            </Container>
            <Container className="m-5 how-section">
                <h1 className="m-2">How does it Work?</h1>
                <h6 className="text-muted mb-5">Quantify how healthy your food items are just by its upc code</h6>
                
                <Row>
                    <Col>
                        <img src={barcode} alt="barcode"></img>
                    </Col>
                    <Col>
                        <div className="info-text m-5">
                            <h1>Scan or Enter Your UPC Code</h1>
                            <p className="text-muted"> Using the camera button or the input, scan or enter the numbers on the barcode. You can find this barcode attached to the food item.</p>
                        </div>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <div className="info-text m-5">
                            <h1>Wait For the Model To Run</h1>
                            <p> Our model will use the UPC code to find the ingredients present in the item. Then we scan over thousands of links and use Semantic Machine Learning to determine how healthy each ingredient is. Finally we assign a score to each ingredient</p>
                        </div>
                    </Col>
                    <Col>
                        <img className="p-4" src={links} alt="links"></img>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <img src={score} alt="score"></img>
                    </Col>
                    <Col>
                        <div className="info-text m-5">
                            <h1>Get your Results</h1>
                            <p> Find a breakdown of all the individual health scores associated with the ingredients in your product. Also find the health score assigned to the food item. The larger the healthscore the more healthy the item is. Therefore, you can interpret the healthscore to judge how healthy your product is.</p>
                        </div>
                    </Col>
                </Row>
                <div className="text-center mt-5 pt-5">
                    <h1>Try it Now</h1>
                    <Link to="/results">
                        <Button className="try-btn"size="lg">
                            Get Started
                        </Button>
                    </Link>
                </div>
            </Container>
            <footer className="b-footer">
                <div className="support-text">
                    <h6>Supported by</h6>
                    <p>aicamp.org</p>
                </div>
            </footer>
            
        </div>
        
    );
}

export default Home;
