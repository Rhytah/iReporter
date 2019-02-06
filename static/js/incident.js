const form = document.getElementById('usrform');
form.addEventListener('submit', addRedflag)
const redflag_url = 'http://127.0.0.1:5000/api/v2/red-flags/'
let authorization_header = 'Bearer '.concat(localStorage.getItem('token'));
let redflag_location  = document.getElementById('location')
let image  = document.getElementById('image')
let video  = document.getElementById('video')
let comment  = document.getElementById('comment')

let invalid = document.getElementById('invalid')

// var x = document.getElementById("location");
function initCoords(position){
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(initialize, locatioError);

    }else{
        showError("Your browser does not support Geolocation!");
    }
}
// function getLocation() {
//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showPosition);
//   } else { 
//     location.innerHTML = "Geolocation is not supported by this browser.";
//   }
// }

function showPosition(position) {
 location.innerHTML = "Latitude: " + lat + 
  "<br>Longitude: " + long;
}

function addRedflag(event){
    event.preventDefault()
    let redflag ={
        location:redflag_location.value,
        image: image.value,
        video: video.value,
        comment: comment.value
    }

fetch(redflag_url,{
    method:'POST',
    mode: 'cors',
    headers :{'content_type':'application/json','Authorization':authorization_header},
    body : JSON.stringify(redflag)  
})
.then ((response) => response.json())
    .then((data) => {
        if(data.message === 'Successfully added red-flag'){
            invalid.textContent = '' + data.message
            window.location.reload()
        }else{
            invalid.textContent = '' + data.message
        }
        console.log(data)
    })
    .catch((err) => console.log(err), invalid.textContent = "something went wrong")
}

// intervention
const intervention_form= document.getElementById('addintervention');
intervention_form.addEventListener('submit',addIntervention)
let intervention_comment = document.getElementById('intervention_comment')
let intervention_location = document.getElementById('lat')
let intervention_image = document.getElementById('image_path')
let intervention_video = document.getElementById('video_path')

const intervention_url = 'http://127.0.0.1:5000/api/v2/interventions/'

function addIntervention(event){
    event.preventDefault()
    let intervention = {
        location:intervention_location.value,
        image: intervention_image.value,
        video: intervention_video.value,
        comment: intervention_comment.value

    }


fetch(intervention_url,{
    method:'POST',
    mode: 'cors',
    headers :{'content_type':'application/json','Authorization':authorization_header},
    body : JSON.stringify(intervention)  
})
.then ((response) => response.json())
    .then((data) => {
        if(data.message === 'Successfully added intervention'){
            invalid.textContent = '' + data.message
            window.location.reload()
        }else{
            invalid.textContent = '' + data.message
        }
        console.log(data)
    })
    .catch((err) => console.log(err), invalid.textContent = "something went wrong")
}