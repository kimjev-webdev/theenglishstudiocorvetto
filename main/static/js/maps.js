// static/js/maps.js

function initMap() {
  const businessLocation = { lat: 45.44110705149633, lng: 9.220700957234282 };

  const map = new google.maps.Map(document.getElementById("map"), {
    center: businessLocation,
    zoom: 16,
    mapId: "2e3879b57b31501dd7f256c3", // 👈 Replace this with your real Map ID!
  });

  const pinImage = document.createElement("img");
  pinImage.src = "/static/images/map_pin.webp";
  pinImage.style.width = "90px";
  pinImage.style.height = "120px";

  new google.maps.marker.AdvancedMarkerElement({
    map,
    position: businessLocation,
    content: pinImage,
    title: "The English Studio"
  });
}

window.initMap = initMap;
