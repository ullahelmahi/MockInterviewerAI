"""
-------------------------------------------------------
Interview Answer Model
-------------------------------------------------------
"""

from datetime import datetime

from app.extensions import db


class InterviewAnswer(db.Model):

    __tablename__ = "interview_answers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    interview_id = db.Column(
        db.Integer,
        db.ForeignKey("interviews.id"),
        nullable=False
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("interview_questions.id"),
        nullable=False
    )

    transcript = db.Column(
        db.Text
    )

    audio_path = db.Column(
        db.String(255)
    )

    video_path = db.Column(
        db.String(255)
    )

    duration = db.Column(
        db.Integer,
        default=0
    )

    confidence_score = db.Column(
        db.Float
    )

    gemini_score = db.Column(
        db.Float
    )

    gemini_feedback = db.Column(
        db.Text
    )

    eye_contact_score = db.Column(
        db.Float
    )

    head_pose_score = db.Column(
        db.Float
    )

    speech_rate = db.Column(
        db.Float
    )

    filler_words = db.Column(
        db.Integer,
        default=0
    )

    pause_count = db.Column(
        db.Integer,
        default=0
    )

    status = db.Column(
        db.String(50),
        default="PENDING"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    question = db.relationship(
        "InterviewQuestion",
        back_populates="answer",
        lazy=True
    )

    voice_score = db.Column(
        db.Float
    )

    voice_fluency = db.Column(
        db.String(50)
    )

    voice_pace = db.Column(
        db.String(50)
    )

    face_detection = db.Column(
        db.Float
    )