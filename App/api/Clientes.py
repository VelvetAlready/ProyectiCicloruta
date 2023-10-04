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

@ruta_cliente.route("/clientes", methods=["POST"])
def create_cliente():
    nombre = request.json.get('nombre')
    if nombre:
        new_cliente = Clientes(nombre=nombre)
        db.session.add(new_cliente)
        db.session.commit()
        return jsonify({"message": "Cliente creado con éxito"})
    else:
        return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400

@ruta_cliente.route("/clientes/<int:id>", methods=["PUT"])
def update_cliente(id):
    nombre = request.json.get('nombre')
    cliente = Clientes.query.get(id)
    if cliente:
        if nombre:
            cliente.nombre = nombre
            db.session.commit()
            return jsonify({"message": "Cliente actualizado con éxito"})
        else:
            return jsonify({"error": "Falta el campo 'nombre' en la solicitud"}), 400
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404

@ruta_cliente.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    cliente = Clientes.query.get(id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"message": "Cliente eliminado con éxito"})
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404
