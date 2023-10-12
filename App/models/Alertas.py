from config.db import app, db, ma

class Alertas(db.Model):
    __tablename__ = "tblAlertas"

    id_alerta = db.Column(db.Integer, primary_key=True)
    Tipo_alerta = db.Column(db.String(50))
    Descripcion_alerta = db.Column(db.String(50))
    Latitud_alerta = db.Column(db.Float)
    Longitud_alerta = db.Column(db.Float)
    Fecha_hora = db.Column(db.Date)

    def __init__(self, Tipo_alerta, Descripcion_alerta, Latitud_alerta, Longitud_alerta, Fecha_hora):
        self.Tipo_alerta = Tipo_alerta
        self.Descripcion_alerta = Descripcion_alerta
        self.Latitud_alerta = Latitud_alerta
        self.Longitud_alerta = Longitud_alerta
        self.Fecha_hora = Fecha_hora

class AlertasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alertas