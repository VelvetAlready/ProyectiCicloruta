from flask import Blueprint, jsonify, request
from config.db import db
from models.Alertas import Alertas, AlertasSchema

ruta_alertas = Blueprint("ruta_alertas", __name__)

alerta_schema = AlertasSchema()
alertas_schema = AlertasSchema(many=True)

@ruta_alertas.route("/alertas", methods=["GET"])
def get_alertas():
    alertas = Alertas.query.all()
    result = alertas_schema.dump(alertas)
    return jsonify(result)

@ruta_alertas.route("/alertas", methods=["POST"])
def create_alerta():
    nombre = request.json.get('nombre')
    if nombre:
        new_alerta = Alertas(nombre=nombre)
        db.session.add(new_alerta)
        db.session.commit()
        return jsonify({"message": "Alerta creada con éxito"})
    else:
        return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400

@ruta_alertas.route("/alertas/<int:id>", methods=["PUT"])
def update_alerta(id):
    nombre = request.json.get('nombre')
    alerta = Alertas.query.get(id)
    if alerta:
        if nombre:
            alerta.nombre = nombre
            db.session.commit()
            return jsonify({"message": "Alerta actualizada con éxito"})
        else:
            return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400
    else:
        return jsonify({"error": "Alerta no encontrada"}), 404

@ruta_alertas.route("/alertas/<int:id>", methods=["DELETE"])
def delete_alerta(id):
    alerta = Alertas.query.get(id)
    if alerta:
        db.session.delete(alerta)
        db.session.commit()
        return jsonify({"message": "Alerta eliminada con éxito"})
    else:
        return jsonify({"error": "Alerta no encontrada"}), 404