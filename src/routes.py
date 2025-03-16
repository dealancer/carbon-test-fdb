from flask import Blueprint, current_app

routes = Blueprint('routes', __name__)
@routes.route("/")
def hello_world():
    current_app.logger.debug('Route "/" has been accessed.')
    return '<h1>Hello, World!</h1><img src="/static/img/flask.png">'

@routes.route("/xyz")
def random_string():
    """Return a random string of 8 characters."""
    current_app.logger.debug('Route "/xyz" has been accessed.')
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return random_str
