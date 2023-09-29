from config.db import app, db, ma

class Inicio(db.Model):
    __tablename__ = "tblinicio"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(500))
    mapa_id = db.Column(db.Integer, db.ForeignKey('tblmapas.id'))
    alertas_id = db.Column(db.Integer, db.ForeignKey('tblalertas.id'))
    comunidad_id = db.Column(db.Integer, db.ForeignKey('tblcomunidad.id'))

    def __init__(self, descripcion, mapa_id, alertas_id, comunidad_id):
        self.descripcion = descripcion
        self.mapa_id = mapa_id
        self.alertas_id = alertas_id
        self.comunidad_id = comunidad_id

with app.app_context():
    db.create_all()

class InicioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'descripcion', 'mapa_id', 'alertas_id', 'comunidad_id')