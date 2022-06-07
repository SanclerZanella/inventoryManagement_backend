import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import jinja_partials
from datetime import datetime


# Reusable extension for SQLAlchemy
db = SQLAlchemy()

def create_app(config_class=Config):
    """
    Create entire instance of the app
    """

    # app initialization and configuration
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

    # Register Partials method
    jinja_partials.register_extensions(app)

    # extensions for app init from above
    db.init_app(app)

    with app.app_context():
      db.create_all()

    # route imports
    from app.routes.index.routes import index_page
    from app.routes.remove.routes import remove_item

    # routes registration
    app.register_blueprint(index_page)
    app.register_blueprint(remove_item)

    return app
