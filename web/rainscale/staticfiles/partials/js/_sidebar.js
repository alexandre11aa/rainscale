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
        mainContainer.style.marginLeft = '0';

        // Altera o ícone para "chevron-right"
        toggleBtn.querySelector('i').classList.remove('bi-chevron-left');
        toggleBtn.querySelector('i').classList.add('bi-chevron-right');

    } else {
        mainContainer.style.marginLeft = '251px';

        // Altera o ícone para "chevron-left"
        toggleBtn.querySelector('i').classList.remove('bi-chevron-right');
        toggleBtn.querySelector('i').classList.add('bi-chevron-left');
    }

    // Atualiza o mapa caso ele exista
    if (typeof map !== 'undefined') {
        setTimeout(() => {
            map.invalidateSize();
        }, 500); // pequeno delay para garantir que o layout foi aplicado
    }
});

document.addEventListener('DOMContentLoaded', function () {
    if (window.innerWidth <= 768) {
        const sidebar = document.querySelector('.sidebar');
        const toggleButton = document.getElementById('sidebarToggle');

        // Garante que a sidebar esteja aberta inicialmente
        sidebar.classList.remove('collapsed');

        // Após 3 segundos, simula o clique no botão para recolher a sidebar
        setTimeout(() => {
            if (toggleButton) {
                toggleButton.click();
            }
        }, 250); // 3 segundos
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
