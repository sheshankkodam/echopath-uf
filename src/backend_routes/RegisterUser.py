from flask_restful import Resource, reqparse
from flask import request
from src.ConfigFactory import ConfigFactory

conf = ConfigFactory.create_app_config()


def validate_first_name(val):
    if not val:
        raise Exception("first name cannot be empty")
    if val.isdigit():
        raise Exception("first name cannot be a number")


def validate_last_name(val):
    if not val:
        raise Exception("last name cannot be empty")
    if val.isdigit():
        raise Exception("last name cannot be a number")


def validate_phone_num(val):
    if not val:
        raise Exception("phone cannot be empty")
    if not val.isdigit():
        raise Exception("phone number cannot be a string")
    if len(val) != 10:
        raise Exception("Not a valid number")


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
        company_name = request.form['companyName']
        print(first_name, last_name, email, password, phone_number, company_name)
        try:
            validate_first_name(first_name)
            validate_last_name(last_name)
            validate_phone_num(phone_number)
            return 'Registration successful'
        except Exception as err:
            return err.message
