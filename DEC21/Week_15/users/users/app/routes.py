import flask
import flask_login
from flask import url_for, request
from flask_babel import gettext
from flask_login import login_manager

from app import app, db, login_mngr, babel
from app.forms import Login, Register
from app.models import User



@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(['de', 'fr', 'en'])
    return 'fr'


@login_mngr.user_loader
def load_user(user_id):
	return User.get(user_id)


@app.route('/')
@flask_login.login_required
def main_page():
	return flask.render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
	if flask_login.current_user.is_authenticated:
		return flask.redirect(url_for('main_page'))

	form = Login()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()

		# Check if it exist and if the password is the right password
		if user is None or not user.password == form.password.data:
			flask.flash('Invalid username or password')
			return flask.redirect(url_for('login'))

		# Log the user in
		flask_login.login_user(user, remember=form.remember_me.data)
		return flask.redirect(url_for('main_page'))

	return flask.render_template('login.html', form=form, name=gettext('name'))


@app.route('/register', methods=["GET", "POST"])
def register():
	form = Register()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return flask.redirect('/login')

	return flask.render_template('register.html', form=form)


@app.route('/logout')
def logout():
	flask_login.logout_user()
	return flask.redirect(url_for('login'))
