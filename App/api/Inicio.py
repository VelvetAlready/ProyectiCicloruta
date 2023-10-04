from flask import Blueprint, jsonify

ruta_inicio = Blueprint("ruta_inicio", __name__)

@ruta_inicio.route("/", methods=["GET"])
def inicio():
    mensaje_bienvenida = "¡Bienvenido a la página sobre Ciclorutas!"
    return jsonify({"message": mensaje_bienvenida})
