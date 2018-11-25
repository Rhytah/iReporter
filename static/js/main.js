
// Get the modal
var modal = document.getElementById('');


function onclick(event) {
    location.href = 'forum.htm'
  }


  function openNav() {
    document.getElementById("mySidenav").style.width = "200px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
// show element on click
function show(id){
    var a = document.getElementById(id);
    if(a.style.display == 'none')
    a.style.display= 'block';
    else
    a.style.display= 'none';
}

// hide element on click
function hide(id){
    var a = document.getElementById(id);
    if(a.style.display == 'block')
    a.style.display= 'none';
    else
    a.style.display= 'block';
}

//open tab 
function opentab(evt, tabName ){
    var t, tabcontent, tablink;
    tabcontent=document.getElementsByClassName('tabcontent');
    for(t=0; t< tabcontent.length; t++){
      tabcontent[t].style.display="none";
    }
    tablink =document.getElementsByClassName('tablink');
    for(t=0; t <tablink.length; t++){
      tablink[t].className = tablink[t].className.replace("active ", "");
    }
    document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += "active";

}

//get geolocation
var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";}
    }
    
function showPosition(position) {
    x.innerHTML="Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
}


