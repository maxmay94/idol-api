from datetime import datetime
from api.models.db import db

class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.String(40), nullable=False)
  text = db.Column(db.Text, nullable=False)
  likes = db.Column(db.Integer)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


  def __init__(self, title, text, likes, user_id):
    self.title = title
    self.text = text
    self.likes = likes
    self.user_id = user_id

  def __repr__(self):
    return f"Post ID: {self.id} -- Date: {self.date} -- Title: {self.title}"