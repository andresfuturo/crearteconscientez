import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { GLTFLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js";

// Escena
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xfdf6e3);

// Cámara
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / 400,
    0.1,
    1000
);
camera.position.set(0, 1.5, 50); // Alejar más

// Renderizador
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, 400);
document.getElementById("contenedor-3d-avatar_agua_femenina").appendChild(renderer.domElement);

// Controles
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.autoRotate = false;

// Luz
const ambientLight = new THREE.AmbientLight(0xffffff, 1);
scene.add(ambientLight);

// Modelo
const loader = new GLTFLoader();
let avatar;

loader.load("/static/models/avatarAguaFemenina.glb", function (gltf) {
    avatar = gltf.scene;
    avatar.scale.set(0.3, 0.3, 0.3);       // Más pequeño
    avatar.position.set(0, -1.5, 0);       // Ajustar verticalmente
    scene.add(avatar);
}, undefined, function (error) {
    console.error("Error al cargar el modelo:", error);
});

// Animación
function animate() {
    requestAnimationFrame(animate);
    if (avatar) avatar.rotation.y += 0.01;
    controls.update();
    renderer.render(scene, camera);
}

animate();
