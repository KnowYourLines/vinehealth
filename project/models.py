from project import db


class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True)
    licence_number = db.Column(db.String(13), unique=False)
