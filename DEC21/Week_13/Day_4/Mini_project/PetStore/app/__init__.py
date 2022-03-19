from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

# Database Connection
db_petstore = {'host': 'localhost',
		   'database': 'pet store',
		   'user': 'postgres',
		   'port': ''}

app.config[
	'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_petstore['user']}@{db_petstore['host']}/{db_petstore['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes