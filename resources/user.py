from flask_restful import Resource,reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    fresh_jwt_required,
    jwt_required)
from models.user import User

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True)
_user_parser.add_argument('password',type=str,required=True)

class UserRegister(Resource):
    def post(self):
        try:
            params = _user_parser.parse_args()
            user = User(None,**params)
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                user.save_to_db()
                return {'message':'User has been created successfully.'}, 200
            except:
                return {'message':'New user was created successfully.'}, 500

class UserResource(Resource):
    @classmethod
    @fresh_jwt_required
    def get(cls,user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'}, 404
        else:
            return user.json(), 201

    @classmethod
    @fresh_jwt_required
    def delete(cls,user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'}, 404
        else:
            user.active=0
            user.save_to_db()
            return {'message': 'User deactivated.'}, 200

class UserLogin(Resource):
    @classmethod
    def post(cls):
        params = _user_parser.parse_args()
        user = User(None,**params)
        db_user = User.find_by_username(user.username)
        if  db_user or db_user.password == user.password:
            access_token = create_access_token(identity=db_user.id, fresh=True)
            refresh_token = create_refresh_token(db_user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 200
        else:
            return {'message':'Invalid credentials'}, 401

class UserLogout(Resource):
    @jwt_required
    def post(self):
        pass

class TokenReferesh(Resource):
    @jwt_refresh_token_required
    def post(self):
        user_id = get_jwt_identity()
        new_token = create_access_token(identity=user_id, fresh=False)
        return {'access_token': new_token}, 200



