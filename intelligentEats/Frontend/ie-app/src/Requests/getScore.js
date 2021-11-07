
async function getScore(upc){
    
    var formdata = new FormData();
    formdata.append("upc", upc);

    var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    };


    // let info_list = {};

    await fetch(`http://localhost:8000/upc/${upc}`, requestOptions)
    .then(response => response.text())
    .then(response => {
        console.log(response)
        // response =  JSON.parse(response)
        // info_list = response;


        // console.log("1" + JSON.stringify(info_list));
        
        // console.log(info_list)
    })
    .catch(error => console.log('error', error));

    // console.log("2" + JSON.stringify(info_list));
    // return final_list;
    // console.log(info_list);
    return [];
}


export default getScore;

