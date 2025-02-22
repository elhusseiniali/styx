import pytest

from config import TestConfig
from styx import create_app, db


@pytest.fixture()
def app():
    # Set the Testing configuration prior to creating the Flask application
    app = create_app(TestConfig)

    return app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def init_database(app):
    """Initialize the test database."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        # Cleanup after tests
        db.session.remove()
        db.drop_all()
