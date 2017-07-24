from flask import render_template, Blueprint

FRONTEND = Blueprint('frontend_routes', __name__, template_folder='templates', static_folder='frontend_static',
                     static_url_path='/frontend_static')
HEADERS = {'Cache-Control': 'private, src-age=0, no-cache',  # "src-age" overrides "expires"
           'Content-type': 'application/json'}


@FRONTEND.route('/', methods=['GET'])
def home():
    return render_template("echopath.html")


@FRONTEND.route('/registerlogin.html', methods=['GET'])
def registerlogin():
    return render_template("registerlogin.html")