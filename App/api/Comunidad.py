from flask import Blueprint, jsonify, request
from config.db import db
from models.Communidad import Communidad, CommunidadSchema

ruta_communidad = Blueprint("ruta_community", __name__)

communidad_schema = CommunidadSchema()
communities_schema = CommunidadSchema(many=True)

@ruta_communidad.route("/communidad", methods=["GET"])
def get_communities():
    communities = Communidad.query.all()
    result = communities_schema.dump(communities)
    return jsonify(result)

@ruta_communidad.route("/communidad", methods=["POST"])
def create_communidad():
    data = request.get_json()
    if data.get('nombre'):
        new_communidad = Communidad(**data)
        db.session.add(new_communidad)
        db.session.commit()
        return jsonify({"message": "Comunidad creada con éxito"})
    else:
        return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400

@ruta_communidad.route("/communidad/<int:id>", methods=["PUT"])
def update_communidad(id):
    nombre = request.json.get('nombre')
    communidad = Communidad.query.get(id)
    if communidad:
        if nombre:
            communidad.nombre = nombre
            db.session.commit()
            return jsonify({"message": "Comunidad actualizada con éxito"})
        else:
            return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400
    else:
        return jsonify({"error": "Comunidad no encontrada"}), 404

@ruta_communidad.route("/communidad/<int:id>", methods=["DELETE"])
def delete_communidad(id):
    communidad = Communidad.query.get(id)
    if communidad:
        db.session.delete(communidad)
        db.session.commit()
        return jsonify({"message": "Comunidad eliminada con éxito"})
    else:
        return jsonify({"error": "Comunidad no encontrada"}), 404
