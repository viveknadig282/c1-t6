import React, {useState, useEffect} from 'react'
import {Fab, TextField, TextareaAutosize, Grid} from '@material-ui/core'
import {ArrowBack, GetApp} from '@material-ui/icons'
import { Link } from "react-router-dom";
// var Barcode = require('react-barcode');
import { useBarcode } from 'react-barcodes'

function BarcodeGenerator(props) {
    const [barcode, setBarcode] = useState('NaN');

    // const handleChange = (event) => {
    //     setBarcode(event.target.value ? event.target.value : '');
    // };

    useEffect(() => {

        setBarcode(props.barcodeVal)
    }, [props])

    const { inputRef } = useBarcode({
        value: barcode,
        options: {
          background: '#ffffff',
        }
    });
    const downloadBarcode = () => {
        const canvas = document.getElementById("mybarcode");
        const pngUrl = canvas
          .toDataURL("image/png")
          .replace("image/png", "image/octet-stream");
        let downloadLink = document.createElement("a");
        downloadLink.href = pngUrl;
        downloadLink.download = "mybarcode.png";
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    };

    return (
      <div>
            {/* <Link to="/">
            <Fab style={{marginRight:10}} color="secondary">
                <ArrowBack/>
            </Fab>
            </Link> */}
            {/* <span>Barcode Generator</span> */}
            
            {/* <div style={{marginTop:30, marginBottom:30}}>
                <TextField onChange={handleChange} style={{width:320}}
                value={barcode} label="Barcode content" size="large" variant="outlined" color="secondary" 
                />
            </div> */}

            <div>
                {
                    barcode !== ''
                    ?
                    <canvas id="mybarcode" ref={inputRef} />
                    :
                    <p>No barcode preview</p>
                }
            </div>
            {/* <div>
                {
                    barcode ? 
                    <GetApp onClick={downloadBarcode} style={{marginLeft:10}}/>:
                    ''
                }
            </div> */}
      </div>
    );
  }
  
  export default BarcodeGenerator;
  