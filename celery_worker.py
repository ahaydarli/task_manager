from core.factories import create_celery

app = create_celery()
app.conf.imports = app.conf.imports
