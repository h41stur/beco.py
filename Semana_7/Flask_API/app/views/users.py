from app import db
from werkzeug.security import generate_password_hash
from flask import jsonify, request
from ..models.users import Users, user_schema, users_schema

# cria usuário
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário criado com sucesso', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'Erro ao criar o usuário', 'data': {}}), 500

# edita o usuário
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'O usuário não existe', 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário atualizado', 'data': result}), 201
    except:
        return jsonify({'message': 'Erro ao atualizar', 'data': {}}), 500

# consulta todos os usuários
def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'Usuários cadastrados', 'data': result}), 201
    return jsonify({'message': 'Nenhum usuario cadastrado', 'data': {}}), 404

# consulta um único usuário
def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário cadastrado', 'data': result}), 201
    return jsonify({'message': 'Nenhum usuario cadastrado', 'data': {}}), 404

# deleta um usuário
def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Nenhum usuario encontrado', 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'Usuário deletado', 'data': result}), 201
        except:
            jsonify({'message': 'Nenhum usuario encontrado', 'data': {}}), 404
# valida usuário pelo username
def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None


