# allows py to interact w/ sqlite3
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
#from flask_jwt import jwt_required


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    # create required name/pw fields
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be blank.")

    def post(self):
        # use the parser / get data from JSON payload
        data = UserRegister.parser.parse_args()

        # find by username
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # connection to database
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # insert values into table. 1st id must be NULL in order to auto-increment. "?"s == username argument, pw argument.
        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(
            table=self.TABLE_NAME)
        # username/pw must be in tuple
        cursor.execute(query, (data['username'], data['password']))

        # save to disk
        connection.commit()
        # close connection
        connection.close()

        return {"message": "User created successfully."}, 201
