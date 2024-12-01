function togglePopup() {
    const popup = document.getElementById("chat-popup");
    const overlay = document.getElementById("chat-popup-overlay");
    const allAnswers = document.querySelectorAll(".faq-answer");
    const allQuestions = document.querySelectorAll(".faq-question");

    
    const isVisible = popup.style.display === "block";
    popup.style.display = isVisible ? "none" : "block";
    overlay.style.display = isVisible ? "none" : "block";

    if (isVisible) {
        allAnswers.forEach(answer => {
            answer.style.display = "none";
        });

        allQuestions.forEach(question => {
            question.classList.remove('selected');
        });
    }
}

function toggleAnswer(element) {
    const allAnswers = document.querySelectorAll(".faq-answer");

    allAnswers.forEach(answer => {
        answer.style.display = "none";
    });
   
    const answer = element.nextElementSibling;
    answer.style.display = answer.style.display === "block" ? "none" : "block";

    const allQuestions = document.querySelectorAll(".faq-question");
    allQuestions.forEach(question => {
        question.classList.remove('selected');
    });
    element.classList.add('selected');
}
