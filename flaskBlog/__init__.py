from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# instantiate a flask application
app = Flask(__name__) # (__name__) indicate the name of the module
app.config['SECRET_KEY'] = 'b16c56c3758a2dc2610fe2f89f3e31ea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# for hashing password
bcrypt = Bcrypt(app)
# Login manager with sessions
login_manager = LoginManager(app)

from flaskBlog import routes