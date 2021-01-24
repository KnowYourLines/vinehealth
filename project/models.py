from project import db


class Licence(db.Model):
    __tablename__ = "licences"
    id = db.Column(db.Integer, primary_key=True)
    licence = db.Column(db.String(13), unique=False)

    def __init__(self, licence=None):
        self.licence = licence

    def __repr__(self):
        return "<Licence %r>" % (self.licence)
