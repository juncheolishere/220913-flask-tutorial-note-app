from . import db # from diary import db
from flask_login import UserMixin
from datetime import datetime

# define User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    notes = db.relationship('Note')
    # 용이성을 위해서 설정된 notes

# define Note Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    datetime = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
