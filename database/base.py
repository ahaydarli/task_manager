from core.extensions import db


class Model(db.Model):
    class Meta:
        database = db.database
