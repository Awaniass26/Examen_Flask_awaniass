from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/todo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        from . import models  
        db.create_all()
        
        from . import views, auth

    return app
