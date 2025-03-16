
from flask import Blueprint, current_app, request, render_template_string

routes = Blueprint('routes', __name__)

@routes.route("/")
def hello_world():
    current_app.logger.debug('Route "/" has been accessed.')
    return '''
        <h1>Hello, World!</h1>
        <img src="/static/img/flask.png">
        <form action="/greet" method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Greet Me</button>
        </form>
    '''

@routes.route("/greet", methods=["POST"])
def greet_user():
    name = request.form.get("name", "World")
    current_app.logger.debug(f'Greet route accessed with name: {name}')
    return render_template_string('''
        <h1>Hello, {{ name }}!</h1>
        <p>Welcome to the Flask app.</p>
        <a href="/">Go back</a>
    ''', name=name)
