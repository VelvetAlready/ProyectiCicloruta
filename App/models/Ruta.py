from config.db import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblrutas"

    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblCliente.id'))
    latitud = db.Column(db.String(250))
    longitud = db.Column(db.String(250))

    def __init__(self, idcliente, latitud, longitud):
        self.idcliente = idcliente
        self.longitud=longitud
        self.latitud=latitud

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idcliente',"latitud","longitud")