
// Get the modal
var modal = document.getElementById('');

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


    var map;
    var geocoder;
    function InitializeMap() {

        var latlng = new google.maps.LatLng(-34.397, 150.644);
        var myOptions =
        {
            zoom: 8,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true
        };
        map = new google.maps.Map(document.getElementById("map"), myOptions);
    }
    