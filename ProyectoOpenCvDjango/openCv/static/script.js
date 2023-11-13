document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('video');
    const capturarAnalizarBtn = document.getElementById('capturarAnalizar');
    const mensajeP = document.getElementById('mensaje');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
        })
        .catch(function (err) {
            console.log("Error: " + err);
        });

    capturarAnalizarBtn.addEventListener('click', function () {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
        procesarImagen(canvas.toDataURL('image/jpeg'));
    });

    function procesarImagen(imagenData) {
        const formData = new FormData();
        formData.append('imagen', dataURLtoFile(imagenData));

        fetch('/procesar', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            detenerAnimacion(); // Detener animación después de recibir la respuesta
            mensajeP.textContent = data.mensaje;
        })
        .catch(error => {
            detenerAnimacion(); // Detener animación en caso de error
        });
    }

    function dataURLtoFile(dataurl) {
        const arr = dataurl.split(',');
        const mime = arr[0].match(/:(.*?);/)[1];
        const bstr = atob(arr[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);
        while (n--) {
            u8arr[n] = bstr.charCodeAt(n);
        }
        return new File([u8arr], 'imagen.jpg', { type: mime });
    }


    function detenerAnimacion() {
        const boton = document.getElementById('capturarAnalizar');
        boton.classList.remove('capturando');
    }

    function updateClock() {
        var now = new Date();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        var seconds = now.getSeconds();
        var timeString ='Hora Actual : ' + hours + ':' + (minutes < 10 ? '0' : '') + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
        $('#clock').text(timeString);
    }

    // Actualizar el reloj inicialmente y cada segundo
    $(document).ready(function() {
        updateClock();
        setInterval(updateClock, 1000);
    });
});
