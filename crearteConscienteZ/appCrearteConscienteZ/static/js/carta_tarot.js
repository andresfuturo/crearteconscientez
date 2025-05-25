document.addEventListener('DOMContentLoaded', function() {
    const cartaEgipcia = document.getElementById('cartaEgipcia');
    const modal = document.querySelector('.modal-tarot'); 

    // Agregar evento para cerrar el modal al hacer clic fuera
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            cerrarModal();
        }
    });

    // Cargar y procesar el JSON de las cartas
    fetch('/static/js/cartas_tarot.json')
        .then(response => response.json())
        .then(data => {
            const cartas = data.cartas;

            cartaEgipcia.addEventListener('click', function() {
                // Rotar la carta
                cartaEgipcia.style.transform = 'rotateY(180deg)';
                cartaEgipcia.style.transition = 'transform 0.6s ease-in-out';

                // Esperar a que termine la rotación
                setTimeout(() => {
                    // Seleccionar una carta aleatoria
                    const cartaSeleccionada = cartas[Math.floor(Math.random() * cartas.length)];

                    // Crear el contenido del modal
                    modal.innerHTML = `
                        <div class="modal-content">
                            <div class="modal-header">
                                <h2>${cartaSeleccionada.nombre}</h2>
                                <button class="close-modal">&times;</button>
                            </div>
                            <div class="modal-body">
                                <div id="carta-revelada" class="carta-revelada">
                                    <img src="${STATIC_URL}${cartaSeleccionada.imagen}" alt="${cartaSeleccionada.nombre}">
                                </div>
                                <div class="carta-info">
                                    <p>${cartaSeleccionada.mensaje}</p>
                                </div>
                            </div>
                        </div>
                    `;

                    // Agregar evento para el botón de cierre
                    const closeButton = modal.querySelector('.close-modal');
                    closeButton.addEventListener('click', function(e) {
                        e.stopPropagation();
                        cerrarModal();
                    });

                    // Mostrar modal
                    modal.style.display = 'flex';
                    modal.style.justifyContent = 'center';
                    modal.style.alignItems = 'center';
                    modal.style.position = 'fixed';
                    modal.style.top = '0';
                    modal.style.left = '0';
                    modal.style.width = '100%';
                    modal.style.height = '100%';
                    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
                    modal.style.zIndex = '1000';

                    // Revertir la rotación
                    cartaEgipcia.style.transform = 'rotateY(0deg)';
                }, 600); // Esperar 600ms para que termine la rotación
            });
        })
        .catch(error => console.error('Error al cargar las cartas:', error));
});

function cerrarModal() {
    const modal = document.querySelector('.modal-tarot');
    modal.style.display = 'none';
    modal.innerHTML = '';
}
