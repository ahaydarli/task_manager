import sys
import os.path as op
import logging

from pathlib import Path
from connexion import FlaskApp
from connexion.resolver import RestyResolver
from flask.logging import default_handler
from core.extensions import db, ma, jwt, celery, cors


settings = {
    "development": "core.settings.DevelopmentConfig",
    "production": "core.settings.ProductionConfig",
    "staging": "core.settings.StagingConfig",
    "testing": "core.settings.TestingConfig",
    "default": "core.settings.DevelopmentConfig",
}


class SettingsError(Exception):
    pass


class SwaggerError(Exception):
    pass


def get_config(setting_name):
    if settings.get(setting_name):
        return settings.get(setting_name)
    else:
        raise SettingsError(f'Given settings name {setting_name} does not exits')


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    return None


def register_api(app):
    app.add_api(Path('api.yaml'),
                resolver=RestyResolver('app.api.controllers'))

    return None


def register_logger(app):
    log_formatter = logging.Formatter(
        "[%(asctime)s] - %(levelname)s - %(name)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    if app.config["DEBUG"]:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
    app.logger.removeHandler(default_handler)
    logging.getLogger('flask_cors').level = logging.DEBUG

    return None


def create_celery(app=None, config='default'):
    app = app or create_app(config)
    celery.conf.update(app.config.get("CELERY", {}))

    class ContextTask(celery.Task):
        """
        Make celery tasks work with Flask app context
        """
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(config_name):
    """
    App factory
    """
    config_obj = get_config(config_name)
    swagger_dir = op.abspath(op.join(op.dirname(__name__), 'api_specs'))
    print(swagger_dir)

    cnnx_app = FlaskApp(__name__, specification_dir=swagger_dir)
    flask_app = cnnx_app.app

    flask_app.config.from_object(config_obj)
    flask_app.app_context().push()

    register_logger(flask_app)
    register_extensions(flask_app)
    register_api(cnnx_app)
    create_celery(flask_app)

    return flask_app
