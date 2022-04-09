from datetime import datetime
from api.models.db import db
from api.models.item import Item
from api.models.post import Post

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    clicks = db.Column(db.Integer)
    items = db.relationship(Item, secondary='link') #  <---------- not too sure about this
    posts = db.relationship(Post, secondary='link') #  <---------- not too sure about this
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return profile