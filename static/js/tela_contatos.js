// Variável global para armazenar as FAQs carregadas
let faqDatabase = [];

// Função para carregar as FAQs do backend
async function loadFAQs() {
    const response = await fetch('/api/faqs/');
    faqDatabase = await response.json();
    console.log('FAQs carregadas:', faqDatabase);
}

// Função para processar a pergunta do usuário// Função para processar a pergunta do usuário
async function processQuestion() {
    if (!faqDatabase.length) {
        alert("As FAQs ainda não foram carregadas.");
        return;
    }

    const userInput = document.getElementById("user-input").value.trim();
    const chatMessages = document.getElementById("chat-messages");

    if (!userInput) return;

    // Adiciona a primeira pergunta do usuário ao chat (sem mensagem do bot inicialmente)
    chatMessages.innerHTML += `
        <div class="message user">
            <div class="avatar">
                <img src="/static/image/perfil.png" alt="Avatar do bot" class="bot-avatar">
            </div>
            <p>${userInput}</p>
        </div>
    `;

    // Normaliza a entrada do usuário para letras minúsculas e divide em palavras
    const normalizedUserInput = userInput.toLowerCase();
    const userWords = normalizedUserInput.split(/\s+/);

    // Procura uma resposta correspondente
    let respostaEncontrada = "Desculpe, não entendi sua pergunta. Por favor, tente novamente.";
    for (const faq of faqDatabase) {
        const normalizedFaq = faq.pergunta.toLowerCase();
        const faqWords = normalizedFaq.split(/\s+/);

        // Verifica se há alguma palavra-chave do usuário nas palavras da pergunta FAQ
        const matchingWords = userWords.filter(word => faqWords.includes(word));

        if (matchingWords.length > 0) {
            respostaEncontrada = faq.resposta;
            break;
        }
    }

    // Adiciona a resposta do bot ao chat
    chatMessages.innerHTML += `
        <div class="message bot">
            <div class="avatar">
                <img src="/static/image/perfil.png" alt="Avatar do bot" class="bot-avatar">
            </div>
            <p>${respostaEncontrada}</p>
        </div>
    `;

    // Limpa o campo de entrada
    document.getElementById("user-input").value = "";

    // Rola para a última mensagem
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
// Detecta Enter pressionado no input
function checkEnter(event) {
    if (event.key === "Enter") {
        processQuestion();
    }
}

// Função para exibir o popup
function togglePopup() {
    const popup = document.getElementById("chat-popup");
    const overlay = document.getElementById("chat-popup-overlay");
    const isVisible = popup.style.display === "flex";
    
    // Alternar a visibilidade do popup e do overlay
    popup.style.display = isVisible ? "none" : "flex";
    overlay.style.display = isVisible ? "none" : "block";
}

// Passando a variável user_avatar corretamente para o JavaScript
const user_avatar = "{{ user_avatar| default:'/static/image/perfil.png' }}";

console.log("user_avatar:", user_avatar);  // Verifique o valor da variável user_avatar

// Carrega as FAQs assim que o script é carregado
loadFAQs();



