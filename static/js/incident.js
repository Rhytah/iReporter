const form = document.getElementById('usrform');
form.addEventListener('submit', addRedflag)
const incident_url = 'http://127.0.0.1:5000/api/v2/red-flags/'
let authorization_header = 'Bearer '.concat(localStorage.getItem('token'));
let redflag_location  = document.getElementById('location')
let image  = document.getElementById('image')
let video  = document.getElementById('video')
let comment  = document.getElementById('comment')

let invalid = document.getElementById('invalid')

// var x = document.getElementById("location");
function initCoords(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(initialize, locatioError);

    }else{
        showError("Your browser does not support Geolocation!");
    }
}
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    location.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
 location.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}

function addRedflag(event){
    event.preventDefault()
    let redflag ={
        location:redflag_location.value,
        image: image.value,
        video: video.value,
        comment: comment.value
    }

fetch(incident_url,{
    method:'POST',
    mode: 'cors',
    headers :{'content_type':'application/json','Authorization':authorization_header},
    body : JSON.stringify(redflag)  
})
.then ((response) => response.json())
    .then((data) => {
        if(data.message === 'Redflag successfully added'){
            invalid.textContent = '' + data.message
            window.location.reload()
        }else{
            invalid.textContent = '' + data.message
        }
        console.log(data)
    })
    .catch((err) => console.log(err), invalid.textContent = "something went wrong")
}