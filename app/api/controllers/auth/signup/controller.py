from connexion import problem
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash

from app.data.models import User


def post(body):
    user_data = body
    user_exists = User.get_or_none(User.email == user_data['email'])
    if user_exists:
        return problem(status=400, title='This email already taken',
                       detail='This email already taken')

    user_data['password'] = generate_password_hash(user_data['password'])
    user = User.create(**user_data)
    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }, 200
