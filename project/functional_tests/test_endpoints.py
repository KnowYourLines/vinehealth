import datetime
import json

from project import app, db
from project.models import Licence


def test_retrieves_all_licence_numbers():
    with app.test_client() as client:
        new_licence = Licence(
            **{
                "last_name": "a",
                "first_name": "b",
                "middle_name": "c",
                "gender": "M",
                "date_of_birth": datetime.date(1999, 9, 9),
            }
        )
        db.session.add(new_licence)
        db.session.flush()
        new_licence = Licence(
            **{
                "last_name": "a",
                "first_name": "b",
                "middle_name": "c",
                "gender": "F",
                "date_of_birth": datetime.date(1999, 9, 9),
            }
        )
        db.session.add(new_licence)
        db.session.flush()
        response = client.get("/licences")
        response = json.loads(response.data)
        assert len(response) == 2
        assert set(response) == {"a9999909099bc", "a9999914099bc"}


def test_stores_new_licence_numbers():
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

        response = client.get("/licences")
        response = json.loads(response.data)
        assert len(response) == 1
        assert set(response) == {"a9999909099bc"}
