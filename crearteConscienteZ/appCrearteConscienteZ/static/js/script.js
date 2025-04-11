(() => {
    let currentIndex = 0;

    document.addEventListener("DOMContentLoaded", () => {
        const slides = document.querySelectorAll('.carousel-item');
        const totalSlides = slides.length;

        if (totalSlides === 0) return;

        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            currentIndex = (index + totalSlides) % totalSlides;
            slides[currentIndex].classList.add('active');
        }

        window.moveSlide = function (direction) {
            showSlide(currentIndex + direction);
        }

        // Mostrar primer slide
        showSlide(currentIndex);

        // Cambiar automáticamente cada 5 segundos
        setInterval(() => {
            showSlide(currentIndex + 1);
        }, 5000);
    });
})();
