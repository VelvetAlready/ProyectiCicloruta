from config.db import app, db, ma

class Mapa(db.Model):
    __tablename__ = "tblmapas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    latitud = db.Column(db.String(250))
    longitud = db.Column(db.String(250))

    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

with app.app_context():
    db.create_all()

class MapaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'latitud', 'longitud')
