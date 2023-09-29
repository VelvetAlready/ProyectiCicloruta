from config.db import app, db, ma

class Alertas(db.Model):
    __tablename__ = "tblAlertas"

    id_alerta = db.Column(db.Integer, primary_key = True)
    Tipo_alerta = db.Column(db.String(50))
    Descripcion_alerta = db.Column(db.String(50))
    Latitud_alerta = db.Column(db.Integer)
    Longitud_alerta = db.Column(db.Integer)
    Fecha_hora=db.Column(db.Date)

    def __init__(self, tipo_alerta,descripcion,latitud,longitud,fecha):
        self.Tipo_alerta = tipo_alerta
        self.Descripcion_alerta = descripcion
        self.Latitud_alerta = latitud
        self.Longitud_alerta = longitud
        self.Fecha_hora= fecha
with app.app_context():
    db.create_all()

class AlertasSchema(ma.Schema):
    class Meta:
        fields = ('id_alerta', 'tipo_alerta','descripcion_alerta','latitud_alerta','longitud_alerta','fecha_hora')