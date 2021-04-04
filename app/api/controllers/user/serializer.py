from core.extensions import ma
from app.data.models import User


class UserSerializer(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'created_at')

