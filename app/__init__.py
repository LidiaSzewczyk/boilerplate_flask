from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    from app.views.main_views import bp_main
    from app.views.auth_views import bp_auth

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)

    login_manager.session_protection = "strong"
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    db.init_app(app)
    mail.init_app(app)

    Migrate(app, db)

    return app
