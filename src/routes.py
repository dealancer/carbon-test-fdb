from flask import Blueprint, current_app

routes = Blueprint('routes', __name__)
@routes.route("/")
def hello_world():
    current_app.logger.debug('Route "/" has been accessed.')
    return '<h1>Hello, World!</h1><img src="/static/img/flask.png">'

@routes.route("/hello/<name>")
def hello_name(name):
    current_app.logger.debug(f'Route "/hello/{{name}}" has been accessed with name: {name}.')
    return f'<h1>Hello, {name}!</h1>'
