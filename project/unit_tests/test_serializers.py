import datetime
import json
import unittest

from project.serializers import LicenceSchema


class LicenceSchemaTest(unittest.TestCase):
    def test_requires_valid_data(self):
        data = {
            "last_name": "a",
            "first_name": "b",
            "middle_name": "c",
            "gender": "M",
            "date_of_birth": "1999-09-09",
        }
        data = json.dumps(data)
        input = LicenceSchema().loads(data)
        result = LicenceSchema().dump(input)
        print(result)
        assert False

    # def test_extracts_licence_numbers(self):
    #     data = {"licence_number": "abcd", "hello": "world"}
    #     result = LicenceSchema().dump({"licence_number": "abcd", "hello": "world"})
    #     assert result == "abcd"
