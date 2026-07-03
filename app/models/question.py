"""
-------------------------------------------------------
Interview Question Model
-------------------------------------------------------
"""

from datetime import datetime
from sqlalchemy.orm import relationship

from app.extensions import db


class InterviewQuestion(db.Model):

    __tablename__ = "interview_questions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    interview_id = db.Column(
        db.Integer,
        db.ForeignKey("interviews.id"),
        nullable=False
    )

    question_number = db.Column(
        db.Integer,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    difficulty = db.Column(
        db.String(20),
        default="Medium"
    )

    expected_time = db.Column(
        db.Integer,
        default=60
    )

    question_text = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    answer = relationship(
        "InterviewAnswer",
        back_populates="question",
        uselist=False
    )

    def __repr__(self):
        return f"<Question {self.question_number}>"