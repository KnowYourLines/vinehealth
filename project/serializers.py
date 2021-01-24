from project import ma
from project.models import Licence


class LicenceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Licence
        fields = ("licence",)
