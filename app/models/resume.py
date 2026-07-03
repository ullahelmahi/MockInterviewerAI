"""
-------------------------------------------------------
Mock Interview AI
-------------------------------------------------------
File: app/models/resume.py
Purpose: Resume database model.
-------------------------------------------------------
"""

from datetime import datetime

from app.extensions import db


class Resume(db.Model):
    """Resume model."""

    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    original_filename = db.Column(
        db.String(255),
        nullable=False
    )

    target_job = db.Column(
        db.String(150),
        nullable=True
    )

    experience_level = db.Column(
        db.String(50),
        nullable=True,
        default="Entry Level"
    )    

    extracted_text = db.Column(
        db.Text,
        nullable=True
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    
    def __repr__(self):
        return f"<Resume {self.original_filename}>"