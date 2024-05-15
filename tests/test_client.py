from app.routes import get_taxis, app

def test_taxis_status(client):
    """Testing taxis status"""
    response = client.get("/taxis")
    assert response.status_code == 200

