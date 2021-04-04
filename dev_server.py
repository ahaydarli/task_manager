import os

from core.factories import create_app
from core.extensions import db

config_name = os.getenv('APP_SETTINGS', 'default')
app = create_app(config_name)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)
