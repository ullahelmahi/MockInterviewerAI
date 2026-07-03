"""
-------------------------------------------------------
Interview Routes
-------------------------------------------------------
"""

from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.interview import interview
from app.interview.services import create_interview


@interview.route("/start")
@login_required
def generate_interview():

    interview_obj = create_interview(
        current_user.id
    )

    if interview_obj is None:

        flash(
            "Please upload your resume before starting an interview.",
            "warning"
        )

        return redirect(
            url_for("upload.upload_resume")
        )

    return redirect(
        url_for(
            "interview_session.interview",
            interview_id=interview_obj.id
        )
    )