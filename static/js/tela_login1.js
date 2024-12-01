// PERSONALIZAÇÃO DO CAMPO DE CPF.
function formatCPF(campo) {
    let cpf = campo.value.replace(/\D/g, ''); 
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2'); 
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2'); 
    cpf = cpf.replace(/(\d{3})(\d{1,2})$/, '$1-$2'); 
    campo.value = cpf;
} 
