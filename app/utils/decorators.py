from functools import wraps

from connexion import problem
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app.data.models import User


def user_exists():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            email = get_jwt_identity()
            user = User.get_or_none(User.email == email)
            if not user:
                return problem(status=404, title='User does not exists',
                               detail='User does not exists')
            else:
                return fn(*args, **kwargs)

        return decorator

    return wrapper
