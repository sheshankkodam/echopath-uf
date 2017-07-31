from flask import render_template, Blueprint, redirect, url_for

FRONTEND = Blueprint('frontend_routes', __name__, template_folder='templates', static_folder='frontend_static',
                     static_url_path='/frontend_static')
HEADERS = {'Cache-Control': 'private, src-age=0, no-cache',  # "src-age" overrides "expires"
           'Content-type': 'application/json'}


@FRONTEND.route('/', methods=['GET'])
def default():
    return redirect(url_for("frontend_routes.home"))


@FRONTEND.route('/home', methods=['GET'])
def home():
    return render_template("echopath.html")


@FRONTEND.route('/echopath.html', methods=['GET'])
def echopath_html():
    return redirect(url_for("frontend_routes.home"))


@FRONTEND.route('/loogo.html', methods=['GET'])
def loogo_html():
    return redirect(url_for("frontend_routes.loogo"))


@FRONTEND.route('/loogo', methods=['GET'])
def loogo():
    return render_template("loogo.html")


@FRONTEND.route('/register.html', methods=['GET'])
def register_html():
    return redirect(url_for("frontend_routes.register"))


@FRONTEND.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@FRONTEND.route('/feedback.html', methods=['GET'])
def feedback_html():
    return redirect(url_for("frontend_routes.feedback"))


@FRONTEND.route('/feedback', methods=['GET'])
def feedback():
    return render_template("feedback.html")


@FRONTEND.route('/navigation.html', methods=['GET'])
def navigation_html():
    return redirect(url_for("frontend_routes.navigation"))


@FRONTEND.route('/navigation', methods=['GET'])
def navigation():
    return render_template("navigation.html")
