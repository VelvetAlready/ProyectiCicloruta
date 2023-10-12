from flask import Blueprint, jsonify, request
from config.db import db
from models.Clientes import Clientes, ClienteSchema

ruta_cliente = Blueprint("ruta_cliente", __name__)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@ruta_cliente.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Clientes.query.all()
    result = clientes_schema.dump(clientes)
    return jsonify(result)

@ruta_cliente.route("/savecliente", methods=["POST"])
def save_cliente():
    data = request.json
    nuevo_cliente = Clientes(**data)
    db.session.add(nuevo_cliente)
    db.session.commit()
    return cliente_schema.jsonify(nuevo_cliente)

@ruta_cliente.route("/updatecliente/<id>", methods=["PUT"])
def update_cliente(id):
    cliente = Clientes.query.get(id)
    if not cliente:
        return jsonify({"message": "Cliente no encontrado"}), 404

    data = request.json
    cliente.nombre = data.get('nombre', cliente.nombre)

    db.session.commit()
    return cliente_schema.jsonify(cliente)

@ruta_cliente.route("/deletecliente/<id>", methods=["DELETE"])
def delete_cliente(id):
    cliente = Clientes.query.get(id)
    if not cliente:
        return jsonify({"message": "Cliente no encontrado"}), 404

    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)