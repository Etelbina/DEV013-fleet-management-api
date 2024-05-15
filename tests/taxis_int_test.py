from app.routes import get_taxis, app

def test_get_taxis():
    with app.test_request_context(
        "/taxis", query_string={"limit": 1, "page": 1}
    ):
        expected_value = [{"id":21,"plate":"NNEL-8793"}]
        response = get_taxis()
        assert response.json == expected_value

def test_taxi_limit():
    with app.test_request_context(
        "/taxis", query_string={"limit": 10, "page": 3}
    ):
        response = get_taxis()
        assert len(response.json) == 10

def test_taxi_page():
    with app.test_request_context(
        "/taxis", query_string={"limit": 1, "page": 2}
    ):
        expected_value = [{"id":56,"plate":"JIMF-2287"}]
        response = get_taxis()
        assert response.json == expected_value

def test_taxis_status():
    with app.test_request_context(
        "/taxis", query_string={"limit": 1, "page": 1}
    ):
        response = get_taxis()
        assert response.status_code == 200

# hacer mock de db (buscar opcion con flask en ambiente de pruebas)
# o a get