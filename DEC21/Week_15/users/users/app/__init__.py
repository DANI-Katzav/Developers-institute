import flask
import flask_login
import flask_migrate
import flask_sqlalchemy
from flask_babel import Babel

from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

login_mngr = flask_login.LoginManager()
login_mngr.init_app(app)
login_mngr.login_view = 'login'

from app import routes, models

db.create_all()
