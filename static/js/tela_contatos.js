function togglePopup() {
    const popup = document.getElementById("chat-popup");
    const overlay = document.getElementById("chat-popup-overlay");
    const allAnswers = document.querySelectorAll(".faq-answer");
    const allQuestions = document.querySelectorAll(".faq-question");

    // Alternar a exibição do popup
    const isVisible = popup.style.display === "block";
    popup.style.display = isVisible ? "none" : "block";
    overlay.style.display = isVisible ? "none" : "block";

    // Se o popup for fechado, reiniciar o estado das respostas
    if (isVisible) {
        allAnswers.forEach(answer => {
            answer.style.display = "none";
        });

        // Reiniciar as perguntas, desmarcando todas
        allQuestions.forEach(question => {
            question.classList.remove('selected');
        });
    }
}

function toggleAnswer(element) {
    const allAnswers = document.querySelectorAll(".faq-answer");

    // Esconde todas as respostas
    allAnswers.forEach(answer => {
        answer.style.display = "none";
    });

    // Alterna a visibilidade da resposta da pergunta clicada
    const answer = element.nextElementSibling;
    answer.style.display = answer.style.display === "block" ? "none" : "block";

    // Marcar a pergunta como "selecionada" (se necessário)
    const allQuestions = document.querySelectorAll(".faq-question");
    allQuestions.forEach(question => {
        question.classList.remove('selected');
    });
    element.classList.add('selected');
}
