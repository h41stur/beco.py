import os
import string
import random

DIR = os.getcwd()
DEBUG = True

# criando a chave secreta
chave_randomica = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(chave_randomica) for i in range(12))
SECRET_KEY = key

# banco de dados
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DIR + '/database.db'
# se for usar MySQL
# SQLALCHEMY_DATABASE_URI = 'mysql://<usuario>:<senha>@localhost:3306/<database>'
SQLALCHEMY_TRACK_MODIFICATIONS = False
