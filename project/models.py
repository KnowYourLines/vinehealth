from project import db


class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(), unique=False)
    first_name = db.Column(db.String(), unique=False)
    middle_name = db.Column(db.String(), unique=False)
    date_of_birth = db.Column(db.Date(), unique=False)
    gender = db.Column(db.String(1), unique=False)
