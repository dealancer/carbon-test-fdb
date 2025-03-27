
from flask import Blueprint, current_app
from datetime import datetime

routes = Blueprint('routes', __name__)

@routes.route("/")
def hello_world():
    current_app.logger.debug('Route "/" has been accessed.')
    return '<h1>Hello, World!</h1><img src="/static/img/flask.png">'

@routes.route("/example")
def example():
    current_app.logger.debug('Route "/example" has been accessed.')
    return "<h1>Current Date and Time: <em>{}</em></h1>".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
