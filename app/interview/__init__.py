from flask import Blueprint

interview = Blueprint(
    "interview",
    __name__,
    url_prefix="/interview"
)

from app.interview import routes