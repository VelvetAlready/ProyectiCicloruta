from flask import Flask, render_template
from config.db import app
from api.Alertas import ruta_alertas
from api.Clientes import ruta_cliente
from api.Community import ruta_community
from api.Ruta import ruta_ruta

app.register_blueprint(ruta_alertas, url_prefix="/api/alertas")
app.register_blueprint(ruta_cliente, url_prefix="/api/clientes")
app.register_blueprint(ruta_community, url_prefix="/api/community")
app.register_blueprint(ruta_ruta, url_prefix="/api/rutas")

@app.route("/")
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')