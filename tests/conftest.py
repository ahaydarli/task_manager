import pytest

from core.factories import create_app
from core.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    app = create_app("testing")
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()