from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import licence

app = Flask(__name__)
app.config.from_object("app.config.Config")
app.register_blueprint(licence.bp)

db = SQLAlchemy(app)


class Licence(db.Model):
    __tablename__ = "licences"
    id = db.Column(db.Integer, primary_key=True)
    licence = db.Column(db.String(13), unique=False)

    def __init__(self, licence=None):
        self.licence = licence

    def __repr__(self):
        return "<Licence %r>" % (self.licence)


@app.cli.command("create-db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
