import flask

app = flask.Flask(__name__)

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
	return "Hello, World!"


@app.route('/sayBye/<name>')
def say_bye(name):
	return f'''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {name.title()}!</h1>
        <h1>thank!</h1>
    </body>
</html>'''