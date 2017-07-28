from flask_restful import Resource, reqparse
from flask import request
from src.ConfigFactory import ConfigFactory
from src.Database import Database

conf = ConfigFactory.create_app_config()
db = Database(conf)


def validate_name(val):
    if not val:
        raise Exception("Name cannot be empty")
    if val.isdigit():
        raise Exception("Name cannot be a number")


def validate_email(val):
    if not val:
        raise Exception("Email cannot be empty")
    if ".com" not in val:
        raise Exception("Invalid email. emails should end with .com")


def validate_feedback_text(val):
    if not val:
        if not val:
            raise Exception("Feedback text cannot be empty")
    if len(val) > 40:
        raise Exception("Feedback text cannot extend more than 40 characters")
    if val == "Write something..":
        raise Exception("Enter a valid feedback text")



class Feedback(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, src-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        pass

    def post(self):
        name = request.form['name']
        email = request.form['email']
        feedback_text = request.form['feedbackText']
        try:
            validate_name(name)
            validate_email(email)
            validate_feedback_text(feedback_text)
            db.save_feedback(name, email, feedback_text)
            return "Thanks for the feedback"
        except Exception as err:
            return err.message
