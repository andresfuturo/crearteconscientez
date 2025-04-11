document.addEventListener("DOMContentLoaded", () => {
    const slides = Array.from(document.querySelectorAll(".carousel-item"));
    let currentIndex = 0;

    if (slides.length === 0) {
        console.warn("No se encontraron elementos con la clase .carousel-item");
        return;
    }

    function showSlide(index) {
        slides.forEach(slide => {
            if (slide && slide.classList) {
                slide.classList.remove("active");
            }
        });

        currentIndex = (index + slides.length) % slides.length;

        const currentSlide = slides[currentIndex];
        if (currentSlide && currentSlide.classList) {
            currentSlide.classList.add("active");
        } else {
            console.error("El slide actual es undefined o no tiene classList");
        }
    }

    window.moveSlide = function (direction) {
        showSlide(currentIndex + direction);
    }

    showSlide(currentIndex);

    setInterval(() => {
        showSlide(currentIndex + 1);
    }, 5000);
});
