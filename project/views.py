from flask import request, Blueprint, Response, jsonify

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
    print(new_licence)
    return Response()


@bp.route("/licences", methods=["GET"])
def licences():
    all_licences = Licence.query.all()
    result = LicenceSchema(many=True).dump(all_licences)
    return jsonify(result)
