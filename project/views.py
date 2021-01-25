from flask import request, Blueprint, jsonify

from project import db
from project.models import Driver
from project.serializers import DriverSchema

bp = Blueprint("licence", __name__)


@bp.route("/licence", methods=["POST"])
def licence():
    input = DriverSchema().loads(request.data)
    new_driver = Driver(**input)
    db.session.add(new_driver)
    db.session.commit()
    result = DriverSchema().dump(new_driver)
    return jsonify(result)


@bp.route("/licences", methods=["GET"])
def licences():
    all_licences = Driver.query.all()
    result = DriverSchema(many=True).dump(all_licences)
    return jsonify(result)
