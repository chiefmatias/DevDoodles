from datetime import datetime
import json
import time

from flask import current_app
from flask_login import UserMixin
from authlib.jose import JsonWebSignature

from flaskblog import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        jws = JsonWebSignature()
        protected = {'protected': {'alg': 'HS256'}}
        payload = {'user_id': self.id, 'exp': int(time.time()) + expires_sec}
        secret = current_app.config['SECRET_KEY']
        
        token = jws.serialize_json(protected, payload, secret)
        
        return token
    
    @staticmethod
    def verify_reset_token(token):
        jws = JsonWebSignature()
        decoded_token = jws.deserialize_json(token, current_app.config['SECRET_KEY'])
        payload_decoded = json.loads(decoded_token['payload'])
        exp = payload_decoded['exp']
        
        #Checks if it is expired
        if exp > time.time():    
            user_id = payload_decoded['user_id']
            return User.query.get(user_id)
        else:
            return None
            
            
    def __repr__(self) -> str:
        return f"User({self.username}, {self.email}, {self.image_file})"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"User({self.title}, {self.date_posted})"
 
