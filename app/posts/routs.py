from flask import Blueprint

from posts.controller import (
    store_user_location,
    fetch_recent_posts,
)

posts_api = Blueprint("posts", __name__)
posts_api.add_url_rule(rule="/store_location", view_func=store_user_location, methods=["POST"])
posts_api.add_url_rule(rule="/fetch_posts", view_func=fetch_recent_posts, methods=["GET"])