from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.models import PointsOfInterest

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)

@app.route('/name2/<input>')
def name2(input):
    result = PointsOfInterest(
            name=input
    )
    db.session.add(result)
    return"HI"
    

@app.route('/getall')
def getall():
    
    PointsOfInterest.query.all()
    return"HI"
    