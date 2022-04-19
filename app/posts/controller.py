import requests
from models import Post

from app import db;

from flask import (
    request,
    g,
    jsonify,
)

def store_user_location():
    if request.method == 'POST':
        text = request.form.get('text')
        lat = request.form.get('lat')
        lon = request.form.get('lon')

        if text & lat & lon: 
            new_post_obj = Post(text=text, lat=lat, lon=lon)
            db.session.add(new_post_obj)
            db.session.commit()

            return 'post saved!', 200
        else: 
            return 'pass the right parameters', 400

def fetch_recent_posts(lat, lon):
    return 'fetched recent posts'