import datetime
import json

from project import app, db
from project.models import Licence


def test_gets_stored_licence_numbers():
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
        db.session.commit()
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
        db.session.commit()
        response = client.get("/licences")
        response = json.loads(response.data)
        assert len(response) == 2
        assert set(response) == {"a9999909099bc", "a9999914099bc"}


def test_stores_licence_numbers():
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
