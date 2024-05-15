from app.routes import get_latest_trajectory, app

def test_get_latest():
    with app.test_request_context(
        "/trajectories/latest", query_string={"limit": 1, "page": 1}
    ):
        expected_value = [{"date":"Fri, 08 Feb 2008 17:37:43 GMT","latitude":116.32706,"longitude":39.84801,"plate":"FHLB-7962","taxi_id":6598}]
        response = get_latest_trajectory()
        assert response.json == expected_value

def test_latest_limit():
    with app.test_request_context(
        "/trajectories/latest", query_string={"limit": 3, "page": 3}
    ):
        response = get_latest_trajectory()
        assert len(response.json) == 3

def test_latest_page():
    with app.test_request_context(
        "/trajectories/latest", query_string={"limit": 1, "page": 2}
    ):
        expected_value = [{"date":"Fri, 08 Feb 2008 12:14:46 GMT","latitude":117.11593,"longitude":40.1541,"plate":"HDBL-4695","taxi_id":7088}]
        response = get_latest_trajectory()
        assert response.json == expected_value

def test_latest_status():
    with app.test_request_context(
        "/trajectories/latest", query_string={"limit": 1, "page": 1}
    ):
        response = get_latest_trajectory()
        assert response.status_code == 200

# intentar test con flask test client
# mockear el get
# impersonar psicopg
# mock db