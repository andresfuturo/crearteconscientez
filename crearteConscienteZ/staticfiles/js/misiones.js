document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll(".checkbox-mision");
    const boton = document.querySelector(".btn-misiones");

    function verificarMisiones() {
        const todasMarcadas = [...checkboxes].every(chk => chk.checked);
        if (todasMarcadas) {
            boton.removeAttribute("disabled");
            boton.classList.add("activo");
        } else {
            boton.setAttribute("disabled", "true");
            boton.classList.remove("activo");
        }
    }

    checkboxes.forEach(chk => {
        chk.addEventListener("change", verificarMisiones);
    });
});
