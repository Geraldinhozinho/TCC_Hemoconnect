// Para o campo de doenças
document.addEventListener('DOMContentLoaded', function () {
    const radios = document.querySelectorAll('input[name="doenca"]');
    const campoDoenca = document.getElementById('campo-doenca');
    const doencaInput = document.querySelector('input[name="doenca_det"]'); 

    radios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'sim') { 
                campoDoenca.style.display = 'block';  
                doencaInput.setAttribute('required', 'true'); 
            } else {
                campoDoenca.style.display = 'none'; 
                doencaInput.removeAttribute('required'); 
                doencaInput.value = ''; 
            }
        });
    });
    const selected = document.querySelector('input[name="doenca"]:checked');
    if (selected && selected.value === 'sim') {
        campoDoenca.style.display = 'block';
        doencaInput.setAttribute('required', 'true');
    }
});


// Para dias

document.addEventListener('DOMContentLoaded', function () {
    const disponibilidadeRadios = document.querySelectorAll('input[name="disponibilidade"]'); 
    const campoDias = document.getElementById('campo-dias');
    const diasInput = document.querySelectorAll('input[name="dias"]'); 
    
    function toggleDias() {
        const selecionouSim = Array.from(disponibilidadeRadios).some(radio => radio.checked && radio.value === 'sim');
        campoDias.style.display = selecionouSim ? 'block' : 'none';

        if (!selecionouSim) {
            diasInput.forEach(dia => {
                dia.checked = false; 
            });
        }
    }
    disponibilidadeRadios.forEach(radio => {
        radio.addEventListener('change', toggleDias);
    });
    toggleDias();
});
