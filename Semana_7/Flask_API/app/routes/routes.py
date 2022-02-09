from app import app
from flask import jsonify
from ..views import users, authenticator

@app.route('/', methods=['GET'])
@authenticator.token_required
def root(current_user):
    return jsonify({'message': f'Hello {current_user.username}'})

@app.route('/users', methods=['POST'])
@authenticator.token_required
def post_user(current_user):
    return users.post_user()

@app.route('/users/<id>', methods=['PUT'])
@authenticator.token_required
def update_user(id, current_user):
    return users.update_user(id)

@app.route('/users', methods=['GET'])
@authenticator.token_required
def get_users(current_user):
    return users.get_users()

@app.route('/users/<id>', methods=['GET'])
@authenticator.token_required
def get_user(id, current_user):
    return users.get_user(id)

@app.route('/users/<id>', methods=['DELETE'])
@authenticator.token_required
def delete_user(id, current_user):
    return users.delete_user(id)

@app.route('/auth', methods=['POST'])
def authenticate():
    return authenticator.auth()