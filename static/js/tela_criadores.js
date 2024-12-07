
document.addEventListener('DOMContentLoaded', () => {
    const hamburguer = document.querySelector('.hamburguer');
    const menu = document.querySelector('.itens-baseA');

    hamburguer.addEventListener('click', () => {
        menu.classList.toggle('active'); // Ativa/desativa a classe para exibir/esconder o menu
    });
});
