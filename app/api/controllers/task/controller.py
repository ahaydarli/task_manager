from flask_jwt_extended import jwt_required

from app.api.controllers.task.serializer import TaskSerializer
from app.data.models import Task
from app.tasks import ip_lookup_task
from app.utils.decorators import user_exists

serializer = TaskSerializer()


@jwt_required()
@user_exists()
def post(body):
    task_data = body
    task = ip_lookup_task.apply_async(args=[task_data['ip_address']])
    task_data['task_id'] = task.id
    task = Task.create(**task_data)

    return serializer.dump(task), 200
