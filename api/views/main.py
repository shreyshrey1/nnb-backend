from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest

mod = Blueprint('main', __name__)


@app.route('/')
def mainpage():
    return '<h1>NNB Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    result = PointsOfInterest(
        name="aria"
    )
    mod.add(result)
    return"HI"
    mod.add(result)
    db.session.commit()


