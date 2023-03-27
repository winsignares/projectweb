#importamos las librerias a trabajar
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://root@localhost/ul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'ul27032023'

db = SQLAlchemy(app)
ma = Marshmallow(app)