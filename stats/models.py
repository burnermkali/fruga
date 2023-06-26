from .import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    team = db.Column(db.String(225), unique=True)
    team_nospace = db.Column(db.String(255))
    new_user = db.Column(db.Boolean, default=False)


    def get_id(self):
        return str(self.id)

class Scoresheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(255))
    game_date = db.Column(db.Integer, unique=True)
    game_string = db.Column(db.String)
    league = db.Column(db.String(255))
    where = db.Column(db.String(255))
    home_team = db.Column(db.String(255), nullable=True)
    away_team = db.Column(db.String(255), nullable = True)
    filename = db.Column(db.String(255))




