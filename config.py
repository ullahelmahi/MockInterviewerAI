"""
-------------------------------------------------------
Mock Interview AI
-------------------------------------------------------
File: config.py
Purpose: Central configuration for the application.

-------------------------------------------------------
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ------------------------------------------------------
# Base Directory
# ------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# ------------------------------------------------------
# Load Environment Variables
# ------------------------------------------------------

load_dotenv(BASE_DIR / ".env")


class Config:
    """Base configuration shared by all environments."""

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR / 'instance' / 'mock_interviewer.db'}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Settings
    UPLOAD_FOLDER = BASE_DIR / "uploads"

    # Generated Reports
    REPORT_FOLDER = BASE_DIR / "reports"

    # Temporary Files
    TEMP_FOLDER = BASE_DIR / "temp"

    # Maximum Upload Size (20 MB)
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    # Allowed File Extensions
    ALLOWED_EXTENSIONS = {"pdf", "docx"}

    # Flask
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}