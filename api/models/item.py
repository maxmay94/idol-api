from datetime import datetime
from api.models.db import db
# from api.models.profile import Profile

class Item(db.Model):
  __tablename__ = 'items'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  description = db.Column(db.String(250))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  # owner = db.relationship('Profile', back_populates='items') # <----- Keeping for now just in case
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  def __repr__(self):
    return f"Item('{self.id}', '{self.name}'"

  def serialize(self):
    item = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    return item