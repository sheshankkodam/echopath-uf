from flask import Flask
import urlparse

from frontend_routes import FRONTEND
from flask_restful_swagger import swagger
from backend_routes.AppStatus import AppStatus
from backend_routes.FileUpload import FileUpload
from flask_restful import Api
from src.ConfigFactory import ConfigFactory

conf = ConfigFactory.create_app_config()

app = Flask(__name__)
app.register_blueprint(FRONTEND)

API_BASE = "/api/"
API_VERSION = "v1/"


def with_prefix(api_version, relative_url):
    api_prefix = urlparse.urljoin(API_BASE, api_version)
    return urlparse.urljoin(api_prefix, relative_url)

api2 = swagger.docs(Api(app), apiVersion='1.0',
                    basePath='http://localhost:5000',
                    resourcePath='/',
                    produces=["application/json", "text/html"],
                    api_spec_url='/api/spec',
                    description='soup Backend API')


api2.add_resource(AppStatus, with_prefix(API_VERSION, 'status'))
api2.add_resource(FileUpload, '/upload')

if __name__ == '__main__':
    app.run(host=conf.host, port=conf.port)
