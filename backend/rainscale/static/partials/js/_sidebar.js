// SCRIPT PARA SIDEBAR

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
