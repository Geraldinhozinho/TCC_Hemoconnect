// let currentSlide = 0; // Variável para controlar o slide atual

//     function moveCarousel(direction) {
//         const carousel = document.querySelector('.carrossel2-campanhas'); // Seleciona o carrossel
//         const slides = document.querySelectorAll('.campanhas'); // Seleciona os slides
//         const slideWidth = slides[0].offsetWidth + 20; // Largura de um slide (mais margem de 20px)
//         const maxSlide = slides.length - 4; // Número máximo de slides visíveis (no caso de 4)

//         // Atualiza o slide atual com base na direção
//         currentSlide += direction;

//         // Impede que o slide ultrapasse os limites
//         if (currentSlide < 0) {
//             currentSlide = 0;
//         } else if (currentSlide > maxSlide) {
//             currentSlide = maxSlide;
//         }

//         // Move o carrossel com base no slide atual
//         carousel.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
//     }


