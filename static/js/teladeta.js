let position = 0; // Posição inicial do carrossel
const items = document.querySelectorAll('.posi'); // Seleciona todos os itens do carrossel
const totalItems = items.length;
const visibleItems = 4; // Quantidade máxima de itens visíveis
const carousel = document.querySelector('.carousel');

function moveCarousel(direction) {
    // Calcula o movimento do carrossel
    const newPosition = position + direction;
    
    // Limita o movimento para não sair dos limites
    if (newPosition < 0 || newPosition > totalItems - visibleItems) return;

    // Move o carrossel na direção desejada
    position = newPosition;
    const offset = -(position * 100) / visibleItems;
    carousel.style.transform = `translateX(${offset}%)`;
}
