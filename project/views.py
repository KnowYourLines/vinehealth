from flask import request, Blueprint, Response

from project.models import Licence
from project.serializers import licences_schema

bp = Blueprint("licence", __name__)


@bp.route("/licence", methods=["POST"])
def licence():
    payload = request.data

    last_name = payload["last_name"]
    digit_1_5 = last_name[:6]
    digit_1_5 = digit_1_5 + "".join("9" for _ in range(5 - len(digit_1_5)))

    date_of_birth = payload["date_of_birth"]
    gender = payload["gender"]
    digit_6 = date_of_birth[2]

    month_of_birth = int(date_of_birth.split("-")[1])
    if gender == "F":
        month_of_birth += 5
    digit_7_8 = f"{month_of_birth:02}"
    digit_9_10 = date_of_birth.split("-")[2][:2]
    digit_11 = date_of_birth[3]
    digit_12 = payload["first_name"][0]
    digit_13 = payload["middle_name"][0] or "9"
    licence_number = (
        digit_1_5 + digit_6 + digit_7_8 + digit_9_10 + digit_11 + digit_12 + digit_13
    )


@bp.route("/licences", methods=["GET"])
def licences():
    all_licences = Licence.query.all()
    return Response(licences_schema.dump(all_licences))
