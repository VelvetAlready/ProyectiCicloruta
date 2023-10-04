from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ruta import Ruta, RutaSchema

ruta_ruta = Blueprint("ruta_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

ruta_schema = RutaSchema()
rutas_schema = RutaSchema(many=True)

@ruta_ruta.route("/rutas", methods=["GET"])
def ruta():
    resultall = Ruta.query.all()# Select * from Ruta;
    result = rutas_schema.dump(resultall)
    return jsonify(result)


#Ellery save rutas
@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Ruta(**data))
    db.session.commit()
    return ruta_schema.jsonify(Ruta(**data))
#Hector actualizar Ruta
@ruta_ruta.route("/updateruta", methods=["PUT"])
def updatecliente():
    id = request.json['id']
    latitud = latitud.json['latitud']
    longitud = longitud.json['latitud']
    nruta = ruta.query.get(id) #Select * from ruta where id = id
    nruta.longitud=longitud
    nruta.latitud=latitud
    db.session.commit()
    return "Datos Actualizado con exitos."


@ruta_ruta.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    ruta = ruta.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(ruta))