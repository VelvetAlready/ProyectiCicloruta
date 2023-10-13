// Verificar si el navegador admite geolocalización
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function (position) {
        var latitud = position.coords.latitude;
        var longitud = position.coords.longitude;

        // Mostrar la latitud y longitud en la página (puedes agregar elementos HTML para mostrar estos datos)
        document.getElementById("latitud").textContent = latitud;
        document.getElementById("longitud").textContent = longitud;

        // Crear un objeto con los datos a enviar en formato JSON
        var data = {
            idcliente: 1,
            latitud: latitud,
            longitud: longitud
        };

        // Configurar encabezados para enviar JSON
        var config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        // Realizar una solicitud POST a la API en Python (endpoint "saveruta")
        axios.post('/api/saveruta', JSON.stringify(data), config)
            .then(function (response) {
                console.log('Datos enviados con éxito:', response.data);
            })
            .catch(function (error) {
                console.error('Error al enviar datos:', error);
            });
    });
} else {
    console.log("El navegador no admite la geolocalización.");
}

document.addEventListener('DOMContentLoaded', function () {
    const messageForms = document.querySelectorAll('.chat .conversacion');
    messageForms.forEach(function (messageForm) {
        const messageInput = messageForm.querySelector('.nuevo-mensaje');
        const mensajes = messageForm.querySelectorAll('.mensaje');

        messageForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const messageText = messageInput.value;
            if (messageText.trim() !== '') {
                // Crear un nuevo elemento de mensaje
                const messageElement = document.createElement('div');
                messageElement.className = 'mensaje';
                messageElement.textContent = messageText;
                messageForm.insertBefore(messageElement, messageInput);

                // Limpiar el campo de entrada
                messageInput.value = '';
            }
        });
    });
});