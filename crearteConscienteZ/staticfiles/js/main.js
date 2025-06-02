document.addEventListener('DOMContentLoaded', function () {
    const elementosCarousel = document.querySelectorAll('.carousel');
    const instances = M.Carousel.init(elementosCarousel, {
        padding: 20,
        indicators: true,
        numVisible: 4,
        dist: -50
    });

    // Auto scroll
    setInterval(function () {
        instances.forEach(function (instance) {
            instance.next(); // Cambia al siguiente slide
        });
    }, 2000); // cada 3 segundos
});
