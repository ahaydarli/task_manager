from connexion import problem
from flask_jwt_extended import create_access_token, create_refresh_token

from app.data.models import User


def post(body):
    user_data = body
    email = user_data['email']
    password = user_data['password']
    user = User.get_or_none(User.email == email)
    if not user:
        return problem(status=404, title='User does not exists',
                       detail='User does not exists or password is wrong')
    else:
        if not user.check_password(password):
            return problem(status=400, title='Password is wrong',
                           detail='User does not exists or password is wrong')

    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }, 200
