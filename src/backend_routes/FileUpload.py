from flask_restful import Resource, reqparse
from flask import request
from werkzeug.utils import secure_filename
from os.path import join, exists
import os
from src.ConfigFactory import ConfigFactory

conf = ConfigFactory.create_app_config()


def create_dir(output_directory):
    if not exists(output_directory):
        os.makedirs(output_directory)


def save_avatar(output_directory, avatar_file):
    image_file_name = secure_filename(avatar_file.filename)
    avatar_file.save(join(output_directory, image_file_name))


class FileUpload(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, src-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        pass

    def post(self):
        avatar = request.files['avatar']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        dob = request.form['dateOfBirth']
        output_directory = conf.outputDirectory

        create_dir(output_directory)
        save_avatar(output_directory, avatar)

        return 'file uploaded successfully1'

