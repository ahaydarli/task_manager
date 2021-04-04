import os
from datetime import timedelta

from flask_env import MetaFlaskEnv

project_name = "task_manager"


class Config(metaclass=MetaFlaskEnv):
    """
    Base configuration class. Subclasses should include configurations for
    testing, development and production environments
    """

    DEBUG = True
    ASSETS_DEBUG = False  # not DEBUG
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(32)

    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "/var/tmp/app.%s.log" % project_name

    JWT_SECRET_KEY = 'tuf6ZocScRJpIrN1CE6hyChP82HyEONo'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    CELERY = {
        "broker_url": 'pyamqp://mzsrdevj:dryoQS1U1JFVyKuRQklBi8cMRvPdv3KB@stingray.rmq.cloudamqp.com/mzsrdevj',
        "result_backend": 'rpc:///',
        "celery_imports": ('app.tasks',),
        "celery_track_started": True,
        "celery_ignore_result": False
    }

    IP_DATA_API_KEY = "f5707864531bd96e15cc1469d1dd6051b2e7afd1cfbfedee3a50e2b5"
