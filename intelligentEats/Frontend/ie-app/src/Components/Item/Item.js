import React from 'react';
import './Itemlist.css';

function Item(props){ 
    
    let title;
    let score;
    let description;

    if(props){
        title = props.title;
        score = props.score;
        // description = props.description;

    }
    return(
        <>
        <div id="title-desc">
            <div id="title" className="m-1">{title}</div>
            <div className="text-muted m-1" id="description">{(score >= 0) ? "This is pretty healthy" : "This is not very healthy"}</div>
        </div>
        <h2 id="score">{score}</h2>
        </>
    )
}

export default Item;