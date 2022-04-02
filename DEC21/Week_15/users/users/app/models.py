from app import db
import flask_login


class User(flask_login.UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
