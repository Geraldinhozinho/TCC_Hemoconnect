let currentSlide = 0;

    function moveSlide(direction) {
        const slide = document.getElementById("carousel-slide");
        const slides = document.querySelectorAll(".carousel-image");
        const totalSlides = slides.length;

        currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
        slide.style.transform = `translateX(-${currentSlide * 100}%)`;
    }