from marshmallow import fields, post_dump
from marshmallow.validate import OneOf

from project import ma
from project.models import Licence


class LicenceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Licence
        fields = (
            "licence_number",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
        )

    first_name = fields.String(load_only=True, required=True)
    middle_name = fields.String(load_only=True, required=True)
    last_name = fields.String(load_only=True, required=True)
    date_of_birth = fields.Date(load_only=True, required=True)
    gender = fields.String(validate=OneOf(["M", "F"]), load_only=True, required=True)
    licence_number = fields.Method("make_licence_number", dump_only=True, required=True)

    @post_dump
    def extract_licence_number(self, data, **kwargs):
        return data["licence_number"]

    def make_licence_number(self, data):
        last_name = data.last_name
        date_of_birth = data.date_of_birth.isoformat()
        gender = data.gender
        month_of_birth = int(date_of_birth.split("-")[1])
        year_of_birth = date_of_birth.split("-")[0]
        day_of_month_of_birth = date_of_birth.split("-")[2][:2]
        decade_of_birth = date_of_birth[2]
        if gender == "F":
            month_of_birth += 5

        digit_1_5 = last_name[:6]
        digit_1_5 = digit_1_5 + "".join("9" for _ in range(5 - len(digit_1_5)))
        digit_6 = decade_of_birth
        digit_7_8 = f"{month_of_birth:02}"
        digit_9_10 = day_of_month_of_birth
        digit_11 = year_of_birth[3]
        digit_12 = data.first_name[0]
        digit_13 = data.middle_name[0] or "9"
        licence_number = (
            digit_1_5
            + digit_6
            + digit_7_8
            + digit_9_10
            + digit_11
            + digit_12
            + digit_13
        )
        return licence_number
