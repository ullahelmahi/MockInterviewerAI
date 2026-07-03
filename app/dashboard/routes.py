from flask import render_template
from flask_login import login_required, current_user

from app.dashboard import dashboard
from app.dashboard.services import (
    get_latest_resume,
    get_user_interviews
)


@dashboard.route("/")
@login_required
def dashboard_home():

    resume = get_latest_resume(
        current_user.id
    )

    interviews = get_user_interviews(
        current_user.id
    )

    return render_template(
        "dashboard/dashboard.html",
        resume=resume,
        interviews=interviews
    )