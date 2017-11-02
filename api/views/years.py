from api import app
from flask import Blueprint, request


mod = Blueprint('years', __name__)

@app.route('/years')
def years():
    return "years"
