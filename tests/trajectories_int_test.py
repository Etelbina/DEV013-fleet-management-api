from app.routes import get_trajectories, app

def test_get_trajectories():
    with app.test_request_context(
        "/trajectories", query_string={"limit": 1, "page": 1, "taxi": 6418, "date": '2008-02-02'}
    ):
        expected_value = [{"date":"Sat, 02 Feb 2008 14:25:54 GMT","latitude":116.3043,"longitude":39.9622,"taxi_id":6418}]
        response = get_trajectories()
        assert response.json == expected_value

def test_trajectories_limit():
    with app.test_request_context(
        "/trajectories", query_string={"limit": 10, "page": 3}
    ):
        response = get_trajectories()
        assert len(response.json) == 10

def test_trajectories_page():
    with app.test_request_context(
        "/trajectories", query_string={"limit": 1, "page": 2}
    ):
        expected_value = [{"date":"Sat, 02 Feb 2008 14:30:55 GMT","latitude":116.32259,"longitude":39.96596,"taxi_id":6418}]
        response = get_trajectories()
        assert response.json == expected_value

def test_trajectories_status():
    with app.test_request_context(
        "/trajectories", query_string={"limit": 1, "page": 1}
    ):
        response = get_trajectories()
        assert response.status_code == 200
