from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.controllers.user.serializer import UserSerializer
from app.data.models import User
from app.utils.decorators import user_exists

serializer = UserSerializer()


@jwt_required()
@user_exists()
def search():
    email = get_jwt_identity()
    user = User.get(User.email == email)

    return serializer.dump(user), 200
