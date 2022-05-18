from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskBlog.config import Config


db = SQLAlchemy()
# for hashing password
bcrypt = Bcrypt()
# Login manager with sessions
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# for sending mail
mail = Mail()



def create_app(confg_class=Config):
    # instantiate a flask application
    app = Flask(__name__) # (__name__) indicate the name of the module
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskBlog.users.routes import users
    app.register_blueprint(users)
    from flaskBlog.posts.routes import posts
    app.register_blueprint(posts)
    from flaskBlog.main.routes import main
    app.register_blueprint(main)

    return app
