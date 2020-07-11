import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            full_name=data['full_name'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        return {
            'message': 'Some error occurred. Please try again.'
        }, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

