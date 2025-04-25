import requests
import pytest
from urllib.parse import urljoin

# Configuration
BASE_URL = "https://recrutement.arvea-test.ovh/"
ENDPOINT = "stock/getQuantity"
CSRF_TOKEN = "eyJpdiI6Ijl2SEdGS2dEVDFmZUlFNURqbU9kS0E9PSIsInZhbHVlIjoiaGdkcDFoMGIxS0w1dE5wQ0R4cnNhWU5JOWdFSmNTK0sySlc5NytNWjZESmZKb0FNRFBWNm5ZYUZPb0pyWnY2YzZ5Q0liY2s4bVQxcHNYK25taG5WWE5uU08reDRaRTVjZkFCTUROZnNvQitZQ0pzVDB2OHJZcWpudkV3SGx0bzQiLCJtYWMiOiJiMWFiNzEzZTEyOGNjNDlkYzA1YjJiMjUyNWM4NTQzYmVkNTIyZTM0NTAwYzJiMDA3MDhkZDA1OGZkYzhhN2M5IiwidGFnIjoiIn0%3D"
SESSION_COOKIE = "eyJpdiI6ImlOSWpUVmNlWXgvVFBjcDFUK01DbkE9PSIsInZhbHVlIjoieGI0MThNZjNSVDd2M3plK3pnc1dabE83TUV3akx5d2ZGNjNHUDg5YjZXKzNqbUZnMlFLTnNsTit3V3hscGtpZlM3T1psU2ZiaHVFeG1KWkt0SHczVkN5ei91UUZucGZRbk1aZlFidlJvMzA0dG8zcGd0dmsyU2E2ekJwM3c4bUwiLCJtYWMiOiIxMzRiMjgwYmJiOTVjMjFhMzg5NGFkMmY3NTdiODAyZjNkMDYzZmE0NWU0MTlmZDRmYTc4NmExNzIwYzg0MTUwIiwidGFnIjoiIn0"

def get_authenticated_session():

    session = requests.Session()


    session.cookies.set('XSRF-TOKEN', CSRF_TOKEN)
    session.cookies.set('arvea_tests_recrutement_session', SESSION_COOKIE)


    test_response = session.get(BASE_URL)
    if test_response.status_code != 200:
        pytest.fail("Session initialization failed")

    return session


@pytest.mark.parametrize("product_id,depot_id,expected_status", [
    ("1001", "1", 200),
    ("9999", "1", 404),
    ("1001", "999", 404)
])
def test_stock_availability(product_id, depot_id, expected_status):

    session = get_authenticated_session()

    params = {
        "product_config_id": product_id,
        "stock_type": "depot",
        "depot_id": depot_id
    }

    response = session.get(
        urljoin(BASE_URL, ENDPOINT),
        params=params,
        headers={"X-XSRF-TOKEN": CSRF_TOKEN}
    )

    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert "quantity" in data
        print(f"Available quantity: {data['quantity']}")


if __name__ == "__main__":
    pytest.main(["-v", __file__])