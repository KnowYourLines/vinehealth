import json
import unittest

from marshmallow import ValidationError

from project.models import Driver
from project.serializers import DriverSchema


class DriverSchemaTest(unittest.TestCase):
    def test_serializes_licence_number_correctly(self):
        data = {
            "licence_number": "a9999909099bc",
            "id": 2,
        }
        new_driver = Driver(**data)
        result = DriverSchema().dump(new_driver)
        assert result == "a9999909099bc"

    def test_serializes_licence_number_correctly_for_many_drivers(self):
        data = {
            "licence_number": "a9999909099bc",
            "id": 2,
        }
        new_driver = Driver(**data)
        result = DriverSchema(many=True).dump([new_driver, new_driver])
        assert result == ["a9999909099bc", "a9999909099bc"]

    def test_deserializes_valid_data_correctly(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": "1999-9-9",
        }
        data = json.dumps(data)
        input = DriverSchema().loads(data)
        assert input == {"licence_number": "a9999909099bc"}
        data = {
            "last_name": "aa",
            "first_name": "basdfs",
            "middle_name": "cfasfds",
            "gender": "F",
            "date_of_birth": "1999-09-09",
        }
        data = json.dumps(data)
        input = DriverSchema().loads(data)
        assert input == {"licence_number": "aa999959099bc"}

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
