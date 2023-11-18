import secrets
import os

from flask import current_app, url_for
from flask_mail import Message
from PIL import Image

from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profilepics', picture_fn)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    protected = token['protected']
    signature = token['signature']
    payload = token['payload']


    msg = Message('Password Reset Request',
                  sender=os.environ.get('MAIN_EMAIL'),
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', protected=protected, signature=signature, payload=payload, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)