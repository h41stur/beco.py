from app import app
import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
from .users import user_by_username
import datetime

# função de autenticação
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Não foi possível autenticar',
                        'WWW-Authenticate': 'Basic auth="Login exigido"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'Usuário não encontrado', 'data': {}}), 404

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username,
                            'exp': datetime.datetime.now() + datetime.timedelta(hours=6)},
                            app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'message': 'Validado com sucesso', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=6)}), 200

    return jsonify({'message': 'Não foi possível autenticar',
                        'WWW-Authenticate': 'Basic auth="Login exigido"'}), 500

# função que obriga o usuário ter um token válido
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Um token é necessário', 'data': {}}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'Token inválido ou expirado', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated