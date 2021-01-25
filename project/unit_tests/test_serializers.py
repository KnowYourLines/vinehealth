import datetime
import unittest

from project.models import Driver
from project.serializers import DriverSchema


class LicenceSchemaTest(unittest.TestCase):
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
