import React from 'react';
import Item from './Item';
import './Itemlist.css';

function Itemlist(props){ 

    // maybe use useState
    // let itemList;
    let ingredients = [];

    if(props){
        // itemList = props.list;
        ingredients = [...props.itemList]; 
    }
    console.log(...ingredients);

    
    // const ingredients = [
    //     {
    //         title: "ingredient1",
    //         score: 5.45,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient2",
    //         score: -3.23,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    //     {
    //         title: "ingredient3",
    //         score: 4.57,
    //         description: "etc"
    //     },
    // ]

    
    return(
        <div className="itemList p-3">
            <ul className="items">
                {ingredients.map((value, key) => {
                    return (
                        <li key={key} className="item">
                            {/* <Link to={value.link} className="link"> */}
                            {/* </Link> */}
                            <Item title={value.name} score={value.score}/>
                        </li>
                    )
                }
                )}
            </ul>
        </div>
    )
    
}

export default Itemlist;