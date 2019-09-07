from flask_restful import Resource, reqparse
from models.user import UserModel

BLANK_ERROR = "'{}' cannot be blank."
USER_ALREADY_EXISTS = "A user with that username already exists."
USER_CREATED_SUCCESSFULLY = "User created successfully."


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help=BLANK_ERROR)
    parser.add_argument('password', type=str, required=True,
                        help=BLANK_ERROR)

    @classmethod
    def post(cls):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": USER_ALREADY_EXISTS}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": USER_CREATED_SUCCESSFULLY}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help=BLANK_ERROR)
    parser.add_argument('password', type=str, required=True,
                        help=BLANK_ERROR)

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {'message': 'Invalid credentials'}, 401
