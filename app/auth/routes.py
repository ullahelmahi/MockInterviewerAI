"""
-------------------------------------------------------
Authentication Routes
-------------------------------------------------------
"""

from flask import flash, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.auth.services import authenticate_user, register_user
from flask_login import current_user


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("dashboard.dashboard_home"))

    if form.validate_on_submit():

        user, message = authenticate_user(
            form.email.data,
            form.password.data
        )

        if user:

            login_user(user)

            flash(message, "success")

            return redirect(url_for("dashboard.dashboard_home"))

        flash(message, "danger")

    return render_template(
        "auth/login.html",
        form=form
    )



@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("dashboard.dashboard_home"))

    if form.validate_on_submit():

        success, message = register_user(form)

        if success:

            flash(message, "success")

            return redirect(url_for("auth.login"))

        flash(message, "danger")

    return render_template(
        "auth/register.html",
        form=form
    )


# Logout route
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("You have been logged out successfully.", "success")

    return redirect(url_for("main.home"))