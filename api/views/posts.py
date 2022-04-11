from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.models.db import db
from api.models.post import Post

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['POST'])
def create():
  data=request.get_json()
  item = Post(**data)
  db.session.add(item)
  db.session.commit()
  return jsonify(item.serialize()), 201