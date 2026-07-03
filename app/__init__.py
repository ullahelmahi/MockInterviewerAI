"""
-------------------------------------------------------
Mock Interview AI
-------------------------------------------------------
File: app/__init__.py
Purpose: Flask Application Factory
-------------------------------------------------------
"""

from config import config
from app.extensions import db, login_manager, migrate
from app import models
from flask import Flask, render_template
from app.main import main
from app.auth import auth
from app.dashboard import dashboard
from app.upload import upload
from app.interview_session import interview_session
from app.api import api
from app.reports import reports
from app.interview import interview




def create_app(config_name: str = "development") -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name: Configuration profile
                     (development, production, testing)

    Returns:
        Configured Flask application
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.models.user import User

    # Import routes so they are registered
    from app.main import routes as main_routes
    from app.auth import routes as auth_routes
    from app.dashboard import routes as dashboard_routes
    from app.upload import routes as upload_routes

    app.register_blueprint(interview_session)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(upload)
    app.register_blueprint(api)
    app.register_blueprint(reports)
    app.register_blueprint(interview)


    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    
    return app