// SCRIPT PARA MAPA

// Inicializa o mapa --- >

const map = L.map('map').setView([window.latitude_central, window.longitude_central], 8); // Exemplo: Paraíba

// --- !

// Adiciona o layer do mapa (OpenStreetMap) --- >

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// --- !

// Adiciona pontos ao mapa --- >

// Cria um objeto para mapear fonte -> cor
const coresPorFonte = {};
window.fontes_unicas.forEach(([fonte, cor]) => {
    coresPorFonte[fonte] = cor;
});

// Adiciona pontos ao mapa com cor personalizada usando DivIcon
window.lista_de_pontos.forEach(ponto => {
    const [id, lat, lon, fonte] = ponto;

    // Pega a cor da fonte, ou usa uma cor padrão se não encontrar
    const cor = coresPorFonte[fonte] || '#3388ff';  // azul padrão

    // Usa a primeira letra da fonte para mostrar no marcador
    const letra = fonte.charAt(0).toUpperCase();

    // Cria um ícone personalizado com DivIcon (HTML+CSS)
    const marcadorIcone = L.divIcon({
        html: `<div style="
            background-color: ${cor};
            color: white;
            border-radius: 25%;
            width: 24px;
            height: 24px;
            text-align: center;
            line-height: 24px;
            font-weight: bold;
            border: 2px solid #000;
            box-shadow: 0 0 3px rgba(0,0,0,0.6);
            ">
            ${letra}
        </div>`,
        className: '',  // remove a classe padrão para estilizar à vontade
        iconSize: [24, 24],
        iconAnchor: [12, 12],
        popupAnchor: [0, -15],
    });

    // Cria o marcador
    const marker = L.marker([lat, lon], { icon: marcadorIcone })
        .addTo(map)
        .bindPopup(`Fonte: ${fonte} (${lat}, ${lon})`);

    // Adiciona o listener de clique para preencher os inputs ao clicar no marcador
    marker.on('click', function() {
        document.getElementById('latitude').value = lat.toFixed(6);
        document.getElementById('longitude').value = lon.toFixed(6);
    });
});

// --- !

// Escuta o clique no mapa --- >

map.on('click', function (e) {
    var lat = e.latlng.lat.toFixed(6);
    var lon = e.latlng.lng.toFixed(6);

    // Preenche os campos de input
    document.getElementById('latitude').value = lat;
    document.getElementById('longitude').value = lon;
});

// --- !