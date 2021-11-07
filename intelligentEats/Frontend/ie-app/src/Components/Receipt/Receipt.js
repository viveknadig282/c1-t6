import React from 'react';
import BarcodeGenerator from '../Scanner/BarcodeGenerator';
import './Receipt.css';
function Receipt(props){ 

    

    return(
        <div className="receipt p-3">
            {/*barcodeVal needs to be a string */}
            <BarcodeGenerator barcodeVal={"010801"}/> 
            <p className="success-text">
                SUCCESS!
            </p>
            <h4>Details</h4>
            <ul className="text-left">
                <li className="h6 text-large">
                    apples
                </li>
            </ul>
            <div className="text-muted text-left mt-5">
                Not your item? Try again or Submit a help request
            </div>

        </div>
    )
    
}

export default Receipt;