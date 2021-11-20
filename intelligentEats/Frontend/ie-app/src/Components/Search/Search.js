import React, {Component} from 'react';
import './Search.css';


class Search extends Component {
    constructor(props) {
      super(props);
      this.state = {
        value: ''
      };
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
    }
  
    
    handleSubmit(event) {
      event.preventDefault();

      // window.location.replace("http://localhost:3000/results");

      // let headers = new Headers();

      // headers.append('Access-Control-Allow-Origin', '*');
      // headers.append('Access-Control-Allow-Credentials', 'true');
      // headers.append('Content-Type', 'text/plain');
      
    //   fetch(`http://127.0.0.1:8000/upc/${this.state.value}`,{
    //     method: 'GET',
    //     // headers: headers
    //   })
    //   .then(async (response) => await response.json())
    //   .then(response => {
    //     console.log(response);
    //   })
    //   .catch(error => {
    //     console.log(error);
    //  });
    //   console.log(this.state.value);
    //   fetch('http://127.0.0.1:8000/upc/' + this.state.value).then(response => console.log(response));
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            <input className="search-input p-4" placeholder="Enter A UPC Code..." value={this.state.value} onChange={this.handleChange} />
          </label>
        </form>
      );
    }



}
export default Search;