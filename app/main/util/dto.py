from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'user_id': fields.Integer(description='user identifier'),
        'email': fields.String(required=True, description='user email address'),
        'full_name': fields.String(required=True, description='user name'),
        'password': fields.String(required=True, description='user password'),
        'registered_on': fields.String(description='user registration date')
    })


class EventDto:
    api = Namespace('event', description='event related operations')
    event = api.model('event', {
        'event_id': fields.Integer(description='event identifier'),
        'user_id': fields.Integer(required=True, description='user identifier'),
        'event_name': fields.String(required=True, description='event name'),
        'event_description': fields.String(required=True, description='event description'),
        'date_start': fields.String(required=True, description='event start date'),
        'date_end': fields.String(required=True, description='event end date'),
        'active': fields.Boolean(required=True, description='event state'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
