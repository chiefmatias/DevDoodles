import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_FLASKBLOG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIN_EMAIL')
    MAIL_PASSWORD = os.environ.get('MAIN_EMAIL_PASSWORD')