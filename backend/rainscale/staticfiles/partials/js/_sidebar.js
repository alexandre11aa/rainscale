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

const allRegioes = Array.from(regiaoSelect.options);
const allModelos = Array.from(modeloSelect.options);

paisSelect.addEventListener('change', function () {
    const selectedPaisId = this.value;

    regiaoSelect.innerHTML = '<option value="">Escolher região</option>';
    allRegioes.forEach(opt => {
        if (opt.dataset.pais === selectedPaisId) {
            regiaoSelect.appendChild(opt.cloneNode(true));
        }
    });

    regiaoSelect.disabled = !selectedPaisId;
    modeloSelect.innerHTML = '<option value="">Escolher modelo</option>';
    modeloSelect.disabled = true;
});

regiaoSelect.addEventListener('change', function () {
    const selectedRegiaoId = this.value;

    modeloSelect.innerHTML = '<option value="">Escolher modelo</option>';
    allModelos.forEach(opt => {
        if (opt.dataset.regiao === selectedRegiaoId) {
            modeloSelect.appendChild(opt.cloneNode(true));
        }
    });

    modeloSelect.disabled = !selectedRegiaoId;
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
