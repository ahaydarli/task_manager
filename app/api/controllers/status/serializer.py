from core.extensions import ma
from app.data.models import Task


class TaskSerializer(ma.Schema):
    class Meta:
        model = Task
        fields = ('id', 'task_id')

