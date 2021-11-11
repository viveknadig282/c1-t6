import React, {useState, useEffect} from 'react';
import BarcodeGenerator from '../Scanner/BarcodeGenerator';
import './Receipt.css';
function Receipt(props){ 

    return(
        <div className="receipt p-3">
            {/*barcodeVal needs to be a string */}
            <BarcodeGenerator barcodeVal={(props.upc) ? props.upc : 'NaN'}/> 
            <p className="success-text">
                SUCCESS!
            </p>
            <h4>Details</h4>
            <ul className="text-left">
                <li className="h6 text-large">
                    ID: 0019221
                </li>
                {/* <li className="h6 text-large">
                    Details: Apples
                </li> */}
            </ul>
            <div className="text-muted text-left mt-5">
                Not your item? Try again or Submit a help request
            </div>

        </div>
    )
    
}

export default Receipt;