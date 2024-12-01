function formatCPF(campo) {
    let cpf = campo.value.replace(/\D/g, ''); // Remove tudo que não for número
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2'); // Coloca o primeiro ponto
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2'); // Coloca o segundo ponto
    cpf = cpf.replace(/(\d{3})(\d{1,2})$/, '$1-$2'); // Coloca o traço
    campo.value = cpf;
} 
