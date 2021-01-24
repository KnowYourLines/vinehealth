from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from project import views

app.register_blueprint(views.bp)

from project import models

db.create_all()
db.session.commit()
