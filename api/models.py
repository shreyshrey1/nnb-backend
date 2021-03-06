
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# import and register blueprints
# from api.views import main
# app.register_blueprint(main.mod)

# db = SQLAlchemy()

# this doesn't work 
class PointsOfInterest(db.Model):
    """Points of Interest"""
    __tablename__ = "points_of_interests"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<name {}'.format(self.name)
