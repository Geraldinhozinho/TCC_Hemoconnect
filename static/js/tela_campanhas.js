var Alert = new CustomAlert();

function CustomAlert() {
    this.render = function(campId) {
        document.getElementById('popUpOverlay').classList.remove('hidden');
        document.getElementById('popUpBox').classList.remove('hidden');

        fetch(`/tela_detalhe_camp/${campId}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('tela_detalhe_camp').innerHTML = `
                <div class='teste'>
                    <img class='foto' src="${data.image_url}" alt="Imagem da campanha"  display:flex;" />
                    <div class='ele'>
                        <h3>${data.titulo}</h3>
                        <p>${data.descricao}</p>
                    </div>
                </div>
                    
                `;
            })
            .catch(error => console.error('Erro ao buscar detalhes da campanha:', error));
    };

    this.ok = function() {
        document.getElementById('popUpOverlay').classList.add('hidden');
        document.getElementById('popUpBox').classList.add('hidden');
    };
}
//carrossel
let currentPosition = 0;

function scrollCarousel(direction) {
    const container = document.querySelector('.carrossel2-campanhas');
    const items = container.querySelectorAll('.campanhas'); 
    const itemWidth = items[0].offsetWidth + 20; 
    const maxScroll = container.scrollWidth - container.offsetWidth; 

    currentPosition += direction * itemWidth;

    if (currentPosition < 0) currentPosition = 0;
    if (currentPosition > maxScroll) currentPosition = maxScroll;

    container.style.transform = `translateX(-${currentPosition}px)`;

    const anteriorBtn = document.getElementById('anteriorBtn');
    anteriorBtn.style.display = currentPosition > 0 ? 'block' : 'none';

    const proximoBtn = document.querySelector('.proximo');
    proximoBtn.style.display = currentPosition < maxScroll ? 'block' : 'none';
}

window.onload = function() {
    const anteriorBtn = document.getElementById('anteriorBtn');
    anteriorBtn.style.display = currentPosition > 0 ? 'block' : 'none';

    const container = document.querySelector('.carrossel2-campanhas');
    const maxScroll = container.scrollWidth - container.offsetWidth;
    const proximoBtn = document.querySelector('.proximo');
    proximoBtn.style.display = currentPosition < maxScroll ? 'block' : 'none';
}


