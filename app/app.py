from gevent import monkey
monkey.patch_all()

from flask_compress import Compress
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import jinja_partials


# Reusable extension for SQLAlchemy
db = SQLAlchemy()

# Create Compress with default params
compress = Compress()

def create_app(config_class=Config):
    """
    Create entire instance of the app
    """

    # app initialization and configuration
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

    # Init compress for our Flask app
    compress.init_app(app)

    # Register Partials method
    jinja_partials.register_extensions(app)

    # extensions for app init from above
    db.init_app(app)

    with app.app_context():
      db.create_all()

    # route imports
    from app.routes.index.routes import index_page
    from app.routes.remove.routes import remove_item
    from app.routes.update.routes import update_item
    from app.routes.restore.routes import restore_item
    from app.routes.delete.routes import delete_item

    # routes registration
    app.register_blueprint(index_page)
    app.register_blueprint(remove_item)
    app.register_blueprint(update_item)
    app.register_blueprint(restore_item)
    app.register_blueprint(delete_item)

    return app
