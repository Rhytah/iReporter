const form = document.getElementById('usrform');
form.addEventListener('submit', addRedflag)
const redflag_url = 'https://rhytah-ireporter.herokuapp.com/api/v2/red-flags/'
let authorization_header = 'Bearer '.concat(localStorage.getItem('token'));
let redflag_location  = document.getElementById('location')
let image  = document.getElementById('image')
let video  = document.getElementById('video')
let comment  = document.getElementById('comment')

let invalid = document.getElementById('invalid')

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

let intervention_image = document.getElementById('image_path')
let intervention_video = document.getElementById('video_path')
let intervention_location_latitude = document.getElementById('intervention_location_latitude')
let intervention_location_longitude = document.getElementById('intervention_location_longitude')

const intervention_url = 'http:/https://rhytah-ireporter.herokuapp.com/api/v2/interventions/'

var x = document.getElementById('intervention_combined_location');

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}


function addIntervention(event){
    event.preventDefault()
    let intervention = {
        lat:intervention_location_latitude.value,
        long:intervention_location_longitude.value,
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