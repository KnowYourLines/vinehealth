from flask import request, Blueprint, jsonify

from project import db
from project.models import Licence
from project.serializers import LicenceSchema

bp = Blueprint("licence", __name__)


@bp.route("/licence", methods=["POST"])
def licence():
    input = LicenceSchema().loads(request.data)
    new_licence = Licence(**input)
    db.session.add(new_licence)
    db.session.commit()
    new_licence_number = Licence.query.filter_by(id=new_licence.id).one()
    result = LicenceSchema().dump(new_licence_number)
    return jsonify(result)


@bp.route("/licences", methods=["GET"])
def licences():
    all_licences = Licence.query.all()
    result = LicenceSchema(many=True).dump(all_licences)
    return jsonify(result)
