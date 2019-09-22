from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.user import User

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password',type=str,required=True)

    def post(self):
        try:
            params = UserRegister.parser.parse_args()
            user = User(None,**params)
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                user.save_to_db()
                return {'message':'User has been created successfully.'}, 200
            except:
                return {'message':'New user was created successfully.'}, 500
