"""
-------------------------------------------------------
Resume Upload Blueprint
-------------------------------------------------------
"""

from flask import Blueprint

upload = Blueprint(
    "upload",
    __name__,
    url_prefix="/upload"
)