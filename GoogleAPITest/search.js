const API_KEY = "AIzaSyDul2IY5ZfoIkHaB6Zq0yn0bpJVH29tJnU";
const cx_id = "2c9c56f8f9439c7cd";


function loadClient() {
    gapi.client.setApiKey(`${API_KEY}`);
    return gapi.client.load("https://content.googleapis.com/discovery/v1/apis/customsearch/v1/rest")
        .then(function() { console.log("GAPI client loaded for API"); },
              function(err) { console.error("Error loading GAPI client for API", err); });
  }
  // Make sure the client is loaded before calling this method.

async function execute() {
    var input = document.getElementById('name');

    await loadClient() 

    console.log("input" + input.value);

    return gapi.client.search.cse.list({
        "c2coff": "0",
        "cx": `${cx_id}`,
        "exactTerms": `${input.value}`,
    })
        .then(function(response) {
                // Handle the results here (response.result has the parsed body).
                console.log("Response", response.result.items);
                },
                function(err) { console.error("Execute error", err); });
  }

gapi.load("client");








