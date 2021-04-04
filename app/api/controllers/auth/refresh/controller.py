from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token


@jwt_required(refresh=True)
def post():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return {
        'access_token': access_token
    }, 200
