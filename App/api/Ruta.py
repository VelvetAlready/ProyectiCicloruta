from flask import Blueprint, jsonify, request
from config.db import db
from models.Ruta import Ruta, RutaSchema

ruta_ruta = Blueprint("ruta_ruta", __name__)

ruta_schema = RutaSchema()
rutas_schema = RutaSchema(many=True)

@ruta_ruta.route("/rutas", methods=["GET"])
def get_rutas():
    rutas = Ruta.query.all()
    result = rutas_schema.dump(rutas)
    return jsonify(result)

@ruta_ruta.route("/saveruta", methods=["POST"])
def save_ruta():
    data = request.json
    nueva_ruta = Ruta(**data)
    db.session.add(nueva_ruta)
    db.session.commit()
    return ruta_schema.jsonify(nueva_ruta)

@ruta_ruta.route("/updateruta/<id>", methods=["PUT"])
def update_ruta(id):
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"message": "Ruta no encontrada"}), 404

    data = request.json
    ruta.idcliente = data.get('idcliente', ruta.idcliente)
    ruta.latitud = data.get('latitud', ruta.latitud)
    ruta.longitud = data.get('longitud', ruta.longitud)

    db.session.commit()
    return ruta_schema.jsonify(ruta)

@ruta_ruta.route("/deleteruta/<id>", methods=["DELETE"])
def delete_ruta(id):
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"message": "Ruta no encontrada"}), 404

    db.session.delete(ruta)
    db.session.commit()
    return ruta_schema.jsonify(ruta)