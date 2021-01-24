from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import views
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(views.bp)

db = SQLAlchemy(app)

from app import models

db.create_all()
db.session.commit()
