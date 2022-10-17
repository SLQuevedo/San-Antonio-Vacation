//fetch json file
fetch("data/airportupdated.json")
    .then(response => {
        return response.json();
    })

// Create a map object.
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);



// Looping through the airport Array
for (var i = 0; i < Data.length; i++) {
    var airport = Data[i](0);
    L.marker([airport.latitudeAirport, airport.longitudeAirport])
        .bindPopup(`<h1>${airport.nameAirport}</h1> <hr> <h3>Airport Code: ${airport.codeIataAirport}</h3>`)
        .addTo(myMap);
}
