

from app import app as _app


def test_hello():
    client = _app.test_client()
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200