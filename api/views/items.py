from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.models.db import db
from api.models.item import Item

items = Blueprint('items', 'items')

@items.route('/', methods=['POST'])
def crete():
  data=request.get_json()
  item = Item(**data)
  db.session.add(item)
  db.session.commit()
  return jsonify(item.serialize()), 201