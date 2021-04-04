from peewee import CharField, AutoField, DateTimeField, SQL
from werkzeug.security import generate_password_hash, check_password_hash

from database.base import Model


class User(Model):
    class Meta:
        table_name = 'users'

    id = AutoField()
    name = CharField(null=False)
    email = CharField(null=False)
    password = CharField(null=False)
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Task(Model):
    class Meta:
        table_name = 'tasks'

    id = AutoField()
    task_id = CharField(null=False)
    ip_address = CharField(null=False)
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

