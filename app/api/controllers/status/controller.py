from flask_jwt_extended import jwt_required

from app.api.controllers.task.serializer import TaskSerializer
from app.tasks import ip_lookup_task
from app.utils.constants import statuses
from app.utils.decorators import user_exists

serializer = TaskSerializer()


@jwt_required()
@user_exists()
def get(task_id):
    task = ip_lookup_task.AsyncResult(task_id)
    if task.state == statuses.SUCCESS:
        response = {
            'status': task.state,
            'data': task.info
        }
    else:
        response = {
            'status': task.state,
            'data': {}
        }

    return response, 200
