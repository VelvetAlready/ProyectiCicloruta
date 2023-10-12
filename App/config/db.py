# Aquí colocamos los comandos para la configuración con la base de datos MySQL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Realizar la conexión
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/ingwebul"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "IngeWeb"

# Creamos los objetos para la base de datos
db = SQLAlchemy(app)
ma = Marshmallow(app)