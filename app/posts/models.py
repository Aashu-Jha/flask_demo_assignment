from app import db
from geoalchemy2.types import Geometry

class Post(db.Model):
    __table_args__ = ({"schema": "public"})
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    lat_lon = db.Column(Geometry(geometry_type='POINT', srid=4326))
    lat = db.Column(db.Numeric)
    lon = db.Column(db.Numeric)
    
