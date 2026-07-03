"""
-------------------------------------------------------
Mock Interview AI
-------------------------------------------------------
Authentication Blueprint
-------------------------------------------------------
"""

from flask import Blueprint

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)