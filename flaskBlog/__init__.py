from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate a flask application
app = Flask(__name__) # (__name__) indicate the name of the module
app.config['SECRET_KEY'] = 'b16c56c3758a2dc2610fe2f89f3e31ea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskBlog import routes