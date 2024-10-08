document.addEventListener('DOMContentLoaded', function () {
    const doencaField = document.querySelector('input[name="doenca"]');
    const doencaDetField = document.querySelector('.doenca2');

    doencaField.addEventListener('change', function () {
        // Limpa o campo e remove mensagens de erro se a resposta for "não"
        if (doencaField.value === 'nao') {
            document.querySelector('input[name="doenca_det"]').value = '';
            doencaDetField.querySelector('.error-message')?.remove();
        }
    });
});