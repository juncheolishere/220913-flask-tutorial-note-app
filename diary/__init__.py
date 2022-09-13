from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create DB Connection
db = SQLAlchemy()
DB_NAME = "database.db"

#Create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jc_secret_key'
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import Blueprint
    from .views import views
    from .auth import auth

    # Apply Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app