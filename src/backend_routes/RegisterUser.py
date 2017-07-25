from flask_restful import Resource, reqparse
from flask import request
from src.ConfigFactory import ConfigFactory

conf = ConfigFactory.create_app_config()


class RegisterUser(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, src-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        pass

    def post(self):
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        phone_number = request.form['phoneNumber']
        email = request.form['email']
        password = request.form['password']
        print(first_name, last_name, email, password, phone_number)

        return 'file uploaded successfully1'

