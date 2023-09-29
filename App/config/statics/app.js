if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitud = position.coords.latitude;
        var longitud = position.coords.longitude;

        // Mostrar la latitud y longitud en la página
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

        // Realizar una solicitud POST a la API en Python
        axios.post('api/saveruta', JSON.stringify(data), config)
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