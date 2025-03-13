// Camera switching functionality
document.addEventListener('DOMContentLoaded', function () {
    const cameraStream = document.getElementById('camera-stream');
    const cameraButtons = document.querySelectorAll('.btn-camera');
    const baseUrl = 'http://localhost:8889/camera_';

    // Get camera from URL parameter if provided
    const urlParams = new URLSearchParams(window.location.search);
    const initialCamera = urlParams.get('camera') || '1';

    // Function to switch camera
    function switchCamera(cameraNumber) {
        cameraStream.src = baseUrl + cameraNumber;

        // Update active button
        cameraButtons.forEach(button => {
            if (button.dataset.camera === cameraNumber) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });

        // Update URL without refreshing page
        const newUrl = new URL(window.location);
        newUrl.searchParams.set('camera', cameraNumber);
        history.replaceState(null, '', newUrl);
        
        // Emit custom event for camera change
        document.dispatchEvent(new CustomEvent('cameraChanged', {
            detail: { camera: cameraNumber }
        }));
    }

    // Add click handlers to all camera buttons
    cameraButtons.forEach(button => {
        button.addEventListener('click', function () {
            const cameraNumber = this.dataset.camera;
            switchCamera(cameraNumber);
        });
    });

    // Keyboard shortcuts for switching cameras (1-4 keys)
    document.addEventListener('keydown', function (event) {
        if (event.key >= '1' && event.key <= '4') {
            switchCamera(event.key);
        }
    });

    // Initialize with camera from URL parameter
    switchCamera(initialCamera);
});
