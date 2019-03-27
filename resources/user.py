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

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": USER_ALREADY_EXISTS}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": USER_CREATED_SUCCESSFULLY}, 201
