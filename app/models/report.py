"""
-------------------------------------------------------
Interview Report Model
-------------------------------------------------------
"""

from datetime import datetime

from app.extensions import db


class InterviewReport(db.Model):

    __tablename__ = "interview_reports"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    interview_id = db.Column(
        db.Integer,
        db.ForeignKey("interviews.id"),
        nullable=False,
        unique=True
    )

    overall_score = db.Column(
        db.Float
    )

    technical_score = db.Column(
        db.Float
    )

    communication_score = db.Column(
        db.Float
    )

    behavioral_score = db.Column(
        db.Float
    )

    strengths = db.Column(
        db.Text
    )

    weaknesses = db.Column(
        db.Text
    )

    recommendations = db.Column(
        db.Text
    )

    hiring_recommendation = db.Column(
        db.String(50)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )