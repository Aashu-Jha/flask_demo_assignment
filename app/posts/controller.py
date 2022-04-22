from posts.models import (
    Post
)

from app import db;
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKTElement

from flask import (
    request,
    jsonify,
)

def store_user_location():
    if request.method == 'POST':
        text = request.args.get('text', default='Heeldsfo')
        lat = request.args.get('lat', default=77.011955)
        lon = request.args.get('lon', default=28.619738)

        if text and lat and lon:
            new_post_obj = Post(text=text, lat_lon=WKTElement('POINT({0} {1})'.format(lat, lon), srid=4326), lat=lat, lon=lon)
            db.session.add(new_post_obj)
            db.session.commit()

            return 'post saved!', 200
        else: 
            return 'pass the right parameters', 400

def fetch_recent_posts():
    lat = request.args.get('lat', default= 29)
    lon = request.args.get('lon', default= 77)
    page_no = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    total_posts = db.session.query(Post).filter((db.func.floor(Post.lat) == lat) and (db.func.floor(Post.lon) == lon)).count()

    ans = db.session.query(Post).filter((db.func.floor(Post.lat) == lat) and (db.func.floor(Post.lon) == lon)).order_by(Post.id)
    ans = ans.paginate(page=page_no, per_page=limit, error_out=False)
    d = []
    for item in ans.items:
        point_representation = to_shape(item.lat_lon)
        answer =  "(lon=" + str(point_representation.y) + \
            ", lat=" + str(point_representation.x) + ")"
        d.append({
            "id" : item.id,
            "text": item.text,
            "lat_lon" : answer,
            "lat" : item.lat,
            "lon" : item.lon
        })
        print(d)
    data = {
        'count': total_posts,
        'data' : d
    }
    return jsonify(data), 200