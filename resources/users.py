import json

from flask import jsonify, Blueprint, abort, make_response

from flask_restful import (Resource, Api, reqparse,
                               inputs, fields, marshal,
                               marshal_with, url_for)

import models
from auth import auth

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'id': fields.String,
}

def user_or_404(user_id):
    try:
        user = models.User.get(models.User.id == user_id)
    except models.User.DoesNotExist:
        abort(404)
    else:
        return user


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=True,
            help='No password verification provided',
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        users = [marshal(user, user_fields) for user in models.User.select()]
        return {'users': users}

    def post(self):
        args = self.reqparse.parse_args()
        if args['password'] == args['verify_password']:
            user = models.User.create_user(**args)
            token = user.generate_auth_token()
            return {
                'user': marshal(user, user_fields), 
                'token': token.decode('ascii')
                }, 201
        return make_response(
            json.dumps({
                'error': 'Password and password verification do not match'
            }), 400)

class User(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=False,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=False,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=False,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'current_password',
            required=False,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=False,
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(user_fields)
    def get(self, id):
        return user_or_404(id)
    
    def post(self):
        pass
    
    @auth.login_required
    def put(self):
        pass

    @auth.login_required
    def delete(self):
        pass

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)
api.add_resource(
    User,
    '/user/<int:id>',
    endpoint='user'
)
