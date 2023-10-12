from flask import Blueprint, jsonify, request
from config.db import db
from models.Alertas import Alertas, AlertasSchema

ruta_alertas = Blueprint("ruta_alertas", __name__)

alertas_schema = AlertasSchema()
alerta_schema = AlertasSchema()

@ruta_alertas.route("/alertas", methods=["GET"])
def get_alertas():
    alertas = Alertas.query.all()
    result = alertas_schema.dump(alertas)
    return jsonify(result)

@ruta_alertas.route("/savealerta", methods=["POST"])
def save_alerta():
    data = request.json
    nuevo_alerta = Alertas(**data)
    db.session.add(nuevo_alerta)
    db.session.commit()
    return alerta_schema.jsonify(nuevo_alerta)

@ruta_alertas.route("/updatealerta/<id>", methods=["PUT"])
def update_alerta(id):
    alerta = Alertas.query.get(id)
    if not alerta:
        return jsonify({"message": "Alerta no encontrada"}), 404

    data = request.json
    alerta.Tipo_alerta = data.get('Tipo_alerta', alerta.Tipo_alerta)
    alerta.Descripcion_alerta = data.get('Descripcion_alerta', alerta.Descripcion_alerta)
    alerta.Latitud_alerta = data.get('Latitud_alerta', alerta.Latitud_alerta)
    alerta.Longitud_alerta = data.get('Longitud_alerta', alerta.Longitud_alerta)

    db.session.commit()
    return alerta_schema.jsonify(alerta)

@ruta_alertas.route("/deletealerta/<id>", methods=["DELETE"])
def delete_alerta(id):
    alerta = Alertas.query.get(id)
    if not alerta:
        return jsonify({"message": "Alerta no encontrada"}), 404

    db.session.delete(alerta)
    db.session.commit()
    return alerta_schema.jsonify(alerta)