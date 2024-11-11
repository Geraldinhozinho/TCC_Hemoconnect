// Para o campo de doenças
document.addEventListener('DOMContentLoaded', function () {
    const radios = document.querySelectorAll('input[name="doenca"]');
    const campoDoenca = document.getElementById('campo-doenca');
    const doencaInput = document.querySelector('input[name="doenca_det"]'); // Campo 'doenca_det'

    radios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'sim') {  // Valor em minúsculo conforme definido no CHOICES
                campoDoenca.style.display = 'block';  // Exibe o campo
                doencaInput.setAttribute('required', 'true');  // Torna o campo obrigatório
            } else {
                campoDoenca.style.display = 'none';  // Oculta o campo
                doencaInput.removeAttribute('required');  // Remove a obrigatoriedade
                doencaInput.value = ''; // Limpa o valor
            }
        });
    });

    // Verifica o valor inicial ao carregar a página
    const selected = document.querySelector('input[name="doenca"]:checked');
    if (selected && selected.value === 'sim') {
        campoDoenca.style.display = 'block';
        doencaInput.setAttribute('required', 'true');  // Torna o campo obrigatório
    }
});




document.addEventListener('DOMContentLoaded', function () {
    const disponibilidadeRadios = document.querySelectorAll('input[name="disponibilidade"]'); // Seleciona os botões de rádio para 'disponibilidade'
    const campoDias = document.getElementById('campo-dias'); // Campo para selecionar os dias
    const diasInput = document.querySelector('input[name="dias"]'); // Seleciona o campo 'dias' no formulário

    // Função para verificar a seleção e mostrar ou ocultar o campo de dias
    function toggleDias() {
        // Verifica se o botão "Sim" está selecionado
        const selecionouSim = Array.from(disponibilidadeRadios).some(radio => radio.checked && radio.value === 'sim');

        // Mostra ou oculta o campo de dias com base na seleção
        campoDias.style.display = selecionouSim ? 'block' : 'none';

        // Se "Não" for selecionado, definimos o valor de "dias" como 'Não'
        if (!selecionouSim) {
            // Oculte o campo "dias" e defina um valor para garantir que "não" será enviado
            diasInput.value = 'Não';  // Define 'Não' ou qualquer valor que indique a não disponibilidade
        } else {
            // Se "Sim" foi selecionado, o campo "dias" deve refletir a seleção dos checkboxes
            diasInput.value = '';  // Limpa o valor do campo "dias" se o campo for visível
        }
    }

    // Adiciona um evento de mudança a cada botão de rádio
    disponibilidadeRadios.forEach(radio => {
        radio.addEventListener('change', toggleDias);
    });

    // Executa a função na carga da página, para garantir que o campo esteja correto
    toggleDias();
});
