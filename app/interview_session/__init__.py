"""
-------------------------------------------------------
Interview Session Blueprint
-------------------------------------------------------
"""

from flask import Blueprint

interview_session = Blueprint(
    "interview_session",
    __name__,
    url_prefix="/interview"
)

from app.interview_session import routes