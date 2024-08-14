from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from API_MINI import app

ma = Marshmallow()


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bakery(db.Model):
    __tablename__ = 'Bakery'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)


ma.init_app(app)
