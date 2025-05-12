// SCRIPT PARA MAPA

// Inicializa o mapa
const map = L.map('map').setView([-7.1219, -34.8789], 6); // Exemplo: Paraíba

// Adiciona o layer do mapa (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Escuta o clique no mapa
map.on('click', function (e) {
    var lat = e.latlng.lat.toFixed(6);
    var lon = e.latlng.lng.toFixed(6);

    // Preenche os campos de input
    document.getElementById('latitude').value = lat;
    document.getElementById('longitude').value = lon;
});
