from flask import Blueprint, request, current_app
from flask_restful import Resource, Api
from .util import generate_token

auth_blueprint = Blueprint('auth', __name__)
api = Api(auth_blueprint)


class Register(Resource):
    def post(self):
        content = request.get_json()
        user_model = current_app.config['USER_MODEL']
        user = user_model.create_user(content)
        token_payload = user_model.get_token_payload(user)
        auth_token = generate_token(
            token_payload, current_app.config['SECRET_KEY'])

        return {
            'token': auth_token.decode('utf-8')
        }, 200


class Login(Resource):
    def post(self):
        content = request.get_json()
        user_model = current_app.config['USER_MODEL']
        user = user_model.authenticate(content)

        if user:
            token_payload = user_model.get_token_payload(user)
            auth_token = generate_token(
                token_payload, current_app.config['SECRET_KEY'])
            return {
                'token': auth_token.decode('utf-8')
            }, 201

        return {'message': 'Bad user credentials'}, 400



api.add_resource(Register, '/token-register')
api.add_resource(Login, '/token-login')
