"""
-------------------------------------------------------
Mock Interview AI
-------------------------------------------------------
Authentication Services
-------------------------------------------------------
"""
from app.extensions import db
from app.models.user import User


def email_exists(email: str) -> bool:
    """
    Check whether an email is already registered.
    """

    return User.query.filter_by(email=email).first() is not None


def register_user(form):
    """
    Register a new user.
    """

    if email_exists(form.email.data):
        return False, "Email already exists."

    user = User(
        full_name=form.full_name.data,
        email=form.email.data
    )

    # Hash and store password
    user.set_password(form.password.data)

    db.session.add(user)
    db.session.commit()

    return True, "Account created successfully."

def authenticate_user(email: str, password: str):
    """
    Authenticate a user using email and password.
    """

    user = User.query.filter_by(email=email).first()

    if user is None:
        return None, "No account found with this email."

    if not user.check_password(password):
        return None, "Incorrect password."

    if not user.is_active_user:
        return None, "Your account has been deactivated."

    return user, "Login successful."