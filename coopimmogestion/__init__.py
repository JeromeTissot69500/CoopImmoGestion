import os

from flask import Flask
from .crypt.crypt import bcrypt
from .db.db import db, migrate
from .smtp.smtp import mail
from .schedule.schedule import scheduler
from .config.DevelopmentConfig import DevelopmentConfig
from .config.ProductionConfig import ProductionConfig
from .config.TestingConfig import TestingConfig
from .controller.error_403 import page_forbidden
from .controller.login import login
from .controller.index import index
from .controller.logout import logout
from .controller.account import account
from .controller.apartment import apartment
from .controller.tenant import tenant
from .controller.rental import rental
from .controller.inventory import inventory
from .controller.finance import finance


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    if test_config is None:
        # Set production config when app is deployed
        if os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
    else:
        # load the test config for unit test pytest
        app.config.from_object(test_config)

    # Register views/controllers
    app.register_error_handler(403, page_forbidden)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(index)
    app.register_blueprint(account)
    app.register_blueprint(apartment)
    app.register_blueprint(tenant)
    app.register_blueprint(rental)
    app.register_blueprint(inventory)
    app.register_blueprint(finance)

    # Initialize hashing, db, db migration, schedule, mail
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)
    mail.init_app(app)

    # Start schedule tasks
    with app.app_context():
        scheduler.start()

    return app
