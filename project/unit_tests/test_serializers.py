import datetime
import json
import unittest

from marshmallow import ValidationError

from project.models import Driver
from project.serializers import DriverSchema


class DriverSchemaTest(unittest.TestCase):
    def test_extracts_licence_number_correctly(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": datetime.date(1999, 9, 9),
        }
        new_driver = Driver(**data)
        result = DriverSchema().dump(new_driver)
        assert result == "a9999909099bc"

        data["gender"] = "F"
        new_driver = Driver(**data)
        result = DriverSchema().dump(new_driver)
        assert result == "a9999914099bc"

    def test_extracts_licence_number_correctly_for_many_drivers(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": datetime.date(1999, 9, 9),
        }
        new_driver = Driver(**data)
        result = DriverSchema(many=True).dump([new_driver, new_driver])
        assert result == ["a9999909099bc", "a9999909099bc"]

        data["gender"] = "F"
        new_driver = Driver(**data)
        result = DriverSchema(many=True).dump([new_driver, new_driver])
        assert result == ["a9999914099bc", "a9999914099bc"]

    def test_deserializes_valid_data(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": "1999-9-9",
        }
        data = json.dumps(data)
        input = DriverSchema().loads(data)
        assert input == {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": datetime.date(1999, 9, 9),
        }

    def test_fails_to_deserialize_invalid_data(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "ABCDEFG",
            "date_of_birth": "1999-9-9",
        }
        data = json.dumps(data)
        with self.assertRaises(ValidationError) as e:
            DriverSchema().loads(data)
        assert str(e.exception) == "{'gender': ['Must be one of: M, F.']}"
