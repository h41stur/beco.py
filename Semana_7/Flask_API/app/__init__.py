from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# criando o objeto da API
app = Flask(__name__)

# instancias de banco de dados
db = SQLAlchemy(app)
ma = Marshmallow(app)

# carregando o config.py
app.config.from_object('config')

from .models import users
from .routes import routes

