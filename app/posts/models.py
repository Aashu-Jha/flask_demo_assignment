import imp
from app.utils import db
from geoalchemy import GeoAlchemy

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    lat_lon = db.Column(db.Integer)
    
