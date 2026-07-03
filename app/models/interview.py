"""
-------------------------------------------------------
Interview Model
-------------------------------------------------------
Represents one interview session.
-------------------------------------------------------
"""

from datetime import datetime

from app.extensions import db


class Interview(db.Model):

    __tablename__ = "interviews"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    resume_id = db.Column(
        db.Integer,
        db.ForeignKey("resumes.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    target_job = db.Column(
        db.String(150),
        nullable=False
    )

    experience_level = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="CREATED"
    )

    ai_model = db.Column(
        db.String(50),
        default="gemini-2.5-flash"
    )

    prompt_version = db.Column(
        db.String(20),
        default="v1.0"
    )

    question_count = db.Column(
        db.Integer,
        default=9
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Interview {self.id}>"