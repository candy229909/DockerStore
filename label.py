<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic STL Viewer</title>
    <style>
        #model {
            width: 800px;
            height: 600px;
            border: 1px solid black;
        }
        .active {
            color: red;  // Highlight the active model
        }
    </style>
</head>
<body>
    <div id="model"></div>
    <ul class="feedback">
        <li>Load Next Model</li>
    </ul>

    <script src="https://threejs.org/build/three.js"></script>
    <script src="https://threejs.org/examples/js/loaders/STLLoader.js"></script>
    <script src="https://threejs.org/examples/js/controls/OrbitControls.js"></script>
    <script>
        var camera, scene, renderer, controls, stlLoader, mesh;
        var folder_path = 'https://example.com/path/to/your/';
        var file_names = ['model1.stl', 'model2.stl', 'model3.stl'];  // Example file names
        var currentModelIndex = 0; // Track the current model index

        init();
        loadSTL(currentModelIndex);  // Initially load the first model

        document.querySelector('.feedback li').addEventListener('click', function(e) {
            currentModelIndex = (currentModelIndex + 1) % file_names.length;  // Increment and wrap the index
            loadSTL(currentModelIndex); // Load the model corresponding to the new index
            window.scrollTo(0, document.body.scrollHeight);  // Scroll to the bottom of the page
            e.preventDefault();
        });

        function init() {
            scene = new THREE.Scene();
            scene.background = new THREE.Color('#EAEAEA');

            camera = new THREE.PerspectiveCamera(75, 800 / 600, 0.1, 1000);
            camera.position.z = 50;

            renderer = new THREE.WebGLRenderer();
            renderer.setSize(800, 600);
            document.getElementById('model').appendChild(renderer.domElement);

            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.addEventListener('change', render);

            window.addEventListener('resize', onWindowResize, false);

            stlLoader = new THREE.STLLoader();
        }

        function loadSTL(index) {
            stlLoader.load(folder_path + file_names[index], function (geometry) {
                var material = new THREE.MeshPhongMaterial({ color: 0xB92C2C, specular: 0x111111, shininess: 200 });
                if (mesh) {
                    scene.remove(mesh);  // Remove the current model if it exists
                }
                mesh = new THREE.Mesh(geometry, material);
                mesh.position.set(0, -10, 0);
                mesh.rotation.set(-Math.PI / 2, 0, 0);
                mesh.scale.set(0.3, 0.3, 0.3);

                scene.add(mesh);

                render();
            });
        }

        function onWindowResize() {
            camera.aspect = 800 / 600;
            camera.updateProjectionMatrix();
            renderer.setSize(800, 600);
            render();
        }

        function render() {
            renderer.render(scene, camera);
        }
    </script>
</body>
</html>
