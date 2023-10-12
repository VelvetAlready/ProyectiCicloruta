from flask import Blueprint, jsonify, request
from config.db import db
from models.Community import Community, CommunitySchema

ruta_community = Blueprint("ruta_community", __name__)

community_schema = CommunitySchema()
communities_schema = CommunitySchema(many=True)

@ruta_community.route("/communities", methods=["GET"])
def get_communities():
    communities = Community.query.all()
    result = communities_schema.dump(communities)
    return jsonify(result)

@ruta_community.route("/savecommunity", methods=["POST"])
def save_community():
    data = request.json
    nueva_community = Community(**data)
    db.session.add(nueva_community)
    db.session.commit()
    return community_schema.jsonify(nueva_community)

@ruta_community.route("/updatecommunity/<id>", methods=["PUT"])
def update_community(id):
    community = Community.query.get(id)
    if not community:
        return jsonify({"message": "Community no encontrada"}), 404

    data = request.json
    community.nombre = data.get('nombre', community.nombre)

    db.session.commit()
    return community_schema.jsonify(community)

@ruta_community.route("/deletecommunity/<id>", methods=["DELETE"])
def delete_community(id):
    community = Community.query.get(id)
    if not community:
        return jsonify({"message": "Community no encontrada"}), 404

    db.session.delete(community)
    db.session.commit()
    return community_schema.jsonify(community)