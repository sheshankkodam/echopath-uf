from flask_restful import Resource, reqparse
from flask import request
from src.ConfigFactory import ConfigFactory
from src.Database import Database

conf = ConfigFactory.create_app_config()
db = Database(conf)


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


def validate_email(val):
    if not val:
        raise Exception("email cannot be empty")
    if ".com" not in val:
        raise Exception("Invalid email. emails should end with .com")


def validate_password(val):
    if not val:
        raise Exception("password cannot be empty")


def validate_company_name(val):
    if val == "Enter Company Name":
        raise Exception("Enter a valid company name")


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
        try:
            validate_first_name(first_name)
            validate_last_name(last_name)
            validate_phone_num(phone_number)
            validate_email(email)
            validate_password(password)
            validate_company_name(company_name)
            db.save_user(first_name, last_name, phone_number, email, password, company_name)
            return 'Registration successful'
        except Exception as err:
            return err.message
