from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.Clientes import ruta_cliente
from api.Ruta import  ruta_ruta
from api.Alertas import ruta_alertas

app.register_blueprint(ruta_cliente, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_alertas, url_prefix="/api")

@app.route("/")
def index():
    return render_template('layout.html')

@app.route("/savegps",methods=["POST"])
def savegps():
    latitud  = request.json['latitud']
    longitud = request.json[ 'longitud']
    print(latitud)
    return jsonify(longitud)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')