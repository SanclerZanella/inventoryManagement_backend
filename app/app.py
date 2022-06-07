from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import jinja_partials


# Reusable extension for SQLAlchemy
db = SQLAlchemy()

map_key = Config.MAP_KEY

def create_app(config_class=Config):
    """
    Create entire instance of the app
    """

    # app initialization and configuration
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

    # Register Partials method
    jinja_partials.register_extensions(app)

    # extensions for app init from above
    db.init_app(app)

    # route imports
    from app.routes.index.routes import index_page

    # routes registration
    app.register_blueprint(index_page)

    return app
