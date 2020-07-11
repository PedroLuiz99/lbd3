from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    @api.doc(security="Login_Token")
    @token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<user_id>')
@api.param('user_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    @api.doc(security="Login_Token")
    def get(self, user_id):
        """get a user given its identifier"""
        user = get_a_user(user_id)
        if not user:
            api.abort(404)
        else:
            return user
