"""
-------------------------------------------------------
Resume Upload Routes
-------------------------------------------------------
"""

from flask import flash, redirect, render_template, url_for
from flask_login import login_required
from wtforms import form

from app.upload import upload
from app.upload.forms import ResumeUploadForm
from app.upload.services import save_resume


@upload.route("/", methods=["GET", "POST"])
@login_required
def upload_resume():

    form = ResumeUploadForm()

    if form.validate_on_submit():

        save_resume(
                form.resume.data,
                form.target_job.data,
                form.experience_level.data
            )

        flash("Resume uploaded successfully.", "success")

        return redirect(url_for("dashboard.dashboard_home"))
    print(form.errors)

    return render_template(
        "upload/upload.html",
        form=form
    )