from flask import request, Blueprint, Response

from project.models import Licence
from project.serializers import LicenceSchema

bp = Blueprint("licence", __name__)


@bp.route("/licence", methods=["POST"])
def licence():
    result = LicenceSchema().load(request.data)
    return Response(result)


@bp.route("/licences", methods=["GET"])
def licences():
    all_licences = Licence.query.all()
    result = LicenceSchema(many=True).dump(all_licences)
    return Response(result)
