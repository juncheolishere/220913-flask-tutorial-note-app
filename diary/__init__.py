from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Create DB Connection
db = SQLAlchemy()
DB_NAME = "database.db"

#Create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jc_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import Blueprint
    from .views import views
    from .auth import auth

    # Apply Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Create or Import Database
    from .models import User, Note
    create_database(app)


    return app

# Create or Check Database file
def create_database(app):
    # check db file
    if not path.exists(f'diary/{DB_NAME}'):
        db.create_all(app=app)
        print('>>>> create db')