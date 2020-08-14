import jwt
from flask import current_app, request, g
from functools import wraps


def generate_token(payload, secret):
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            return {'message': 'Unauthorized'}, 401
        data = request.headers['Authorization']
        token = str.replace(str(data), 'Bearer ', '')
        try:
            user = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithm='HS256')
            g.user = user
        except:
            return {'message': 'Unauthorized'}, 401

        return func(*args, **kwargs)

    return wrapper
