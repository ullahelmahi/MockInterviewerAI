"""
-------------------------------------------------------
Resume Upload Form
-------------------------------------------------------
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import SubmitField

from wtforms import (SubmitField,StringField,RadioField)

from wtforms.validators import DataRequired


class ResumeUploadForm(FlaskForm):

    resume = FileField(
        "Resume",
        validators=[
            FileRequired(),
            FileAllowed(
                ["pdf", "docx"],
                "Only PDF and DOCX files are allowed."
            )
        ]
    )

    target_job = StringField(
        "Target Job",
        validators=[DataRequired()]
    )

    experience_level = RadioField(
        "Experience Level",
        choices=[
            ("Internship", "Internship"),
            ("Entry Level", "Entry Level"),
            ("Mid Level", "Mid Level"),
            ("Senior Level", "Senior Level")
        ],
        default="Entry Level",
        validators=[DataRequired()]
    )

    submit = SubmitField("Upload Resume")