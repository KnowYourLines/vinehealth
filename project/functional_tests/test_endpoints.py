import json

from project import app


def test_stores_and_retrieves_new_licence_numbers():
    with app.test_client() as client:
        response = client.post(
            "/licence",
            json={
                "last_name": "a",
                "first_name": "b",
                "middle_name": "c",
                "gender": "M",
                "date_of_birth": "1999-09-09",
            },
        )
        response = json.loads(response.data)
        assert response == "a9999909099bc"

        response = client.post(
            "/licence",
            json={
                "last_name": "a",
                "first_name": "b",
                "middle_name": "c",
                "gender": "F",
                "date_of_birth": "1999-09-09",
            },
        )
        response = json.loads(response.data)
        assert response == "a9999914099bc"

        response = client.get("/licences")
        response = json.loads(response.data)
        assert len(response) == 2
        assert set(response) == {"a9999909099bc", "a9999914099bc"}
