// SCRIPT PARA RECOLHER SIDEBAR

const sidebar = document.querySelector('.sidebar');
const mainContainer = document.querySelector('.main-container');
const sidebarToggle = document.querySelector('.sidebar-toggle');
const toggleBtn = sidebarToggle;

sidebarToggle.addEventListener('click', () => {

    // Alterna a classe 'collapsed' no sidebar
    sidebar.classList.toggle('collapsed');

    // Ajusta o margin-left da main-container de acordo com o estado do sidebar
    if (sidebar.classList.contains('collapsed')) {
        mainContainer.style.marginLeft = '0';  // Quando o sidebar é recolhido, margin-left é 0
        toggleBtn.textContent = '⮞';  // Alterando o texto do botão

    } else {
        mainContainer.style.marginLeft = '251px';  // Quando o sidebar está expandido, margin-left é 251px
        toggleBtn.textContent = '⮜';  // Alterando o texto do botão
    }
});


// SCRIPT PARA SELECIONADOS DINAMICAMENTE

const paisSelect = document.getElementById('paisSelect');
const regiaoSelect = document.getElementById('regiaoSelect');
const modeloSelect = document.getElementById('modeloSelect');

const regiaoDiv = document.getElementById('regiaoDiv');
const modeloDiv = document.getElementById('modeloDiv');

const allRegioes = Array.from(regiaoSelect.options);
const allModelos = Array.from(modeloSelect.options);

paisSelect.addEventListener('change', function () {
    const selectedPaisId = this.value;

    // Reset região
    regiaoSelect.innerHTML = '<option selected disabled>Escolher região</option>';
    modeloSelect.innerHTML = '<option selected disabled>Escolher modelo</option>';
    modeloSelect.disabled = true;
    modeloDiv.classList.add('d-none'); // esconde modelo

    if (selectedPaisId) {
        allRegioes.forEach(opt => {
            if (opt.dataset.pais === selectedPaisId) {
                regiaoSelect.appendChild(opt.cloneNode(true));
            }
        });
        regiaoSelect.disabled = false;
        regiaoDiv.classList.remove('d-none'); // mostra região
    } else {
        regiaoSelect.disabled = true;
        regiaoDiv.classList.add('d-none');
    }
});

regiaoSelect.addEventListener('change', function () {
    const selectedRegiaoId = this.value;

    // Reset modelo
    modeloSelect.innerHTML = '<option selected disabled>Escolher modelo</option>';

    if (selectedRegiaoId) {
        allModelos.forEach(opt => {
            if (opt.dataset.regiao === selectedRegiaoId) {
                modeloSelect.appendChild(opt.cloneNode(true));
            }
        });
        modeloSelect.disabled = false;
        modeloDiv.classList.remove('d-none'); // mostra modelo
    } else {
        modeloSelect.disabled = true;
        modeloDiv.classList.add('d-none');
    }
});


// CONSTRUÇÃO PARA BUSCA

document.addEventListener('DOMContentLoaded', function () {
    const modeloSelect = document.getElementById('modeloSelect');
    const buscarButton = document.getElementById('modeloBuscar');

    modeloSelect.addEventListener('change', function () {
        const selectedOption = this.options[this.selectedIndex];
        const modeloId = selectedOption.value;

        if (modeloId) {
            const url = `/mapa/${modeloId}`;
            buscarButton.href = url;

        } else {
            buscarButton.href = '#';
        }
    });
});
