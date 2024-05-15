import pytest
from app.routes import app

@pytest.fixture()
def client():
    """Client for tests"""
    yield app.test_client()
