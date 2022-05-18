import os

class Config:
    SECRET_KEY = 'b16c56c3758a2dc2610fe2f89f3e31ea'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')