import React, { Component } from 'react';
import Scanner from '../Components/Scanner';
import "./BarcodeScanner.css";
import { Link } from "react-router-dom";

class BarcodeScanner extends Component {
  state = {
    results: [],
  }

  _scan = () => {
    this.setState({ scanning: !this.state.scanning })
  }

  _onDetected = result => {
    this.setState({ results: [] })
    this.setState({ results: this.state.results.concat([result]) })
  }

  render() {
    return (
      <div>
        <span>Barcode Scanner</span>
        
        <div>
          <Scanner onDetected={this._onDetected} />
        </div>

        <div>{this.state.results[0] ? this.state.results[0].codeResult.code : 'No data scanned'}</div>

      </div>
    )
  }
}

export default BarcodeScanner
