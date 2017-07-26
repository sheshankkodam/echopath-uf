from flask_restful import Resource, reqparse
from flask import request
from src.ConfigFactory import ConfigFactory
from src.Database import Database

conf = ConfigFactory.create_app_config()
db = Database(conf)


class RegisterUser(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, src-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        pass

    def post(self):
        pass
