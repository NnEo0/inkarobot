import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r132/build/three.module.js';

function init() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('scene-container').appendChild(renderer.domElement);

    // Agrega tu escena y objetos Three.js aquí

    camera.position.z = 5;

    const animate = function () {
        requestAnimationFrame(animate);

        // Actualiza tu animación aquí

        renderer.render(scene, camera);
    };

    animate();
}

window.onload = init;
