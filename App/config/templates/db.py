from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Realizar la conexiòn
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root@localhost/ingwebul"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "IngeWeb"

#creamos los objetos de transferencias a la bd

db = SQLAlchemy(app)
ma = Marshmallow(app)