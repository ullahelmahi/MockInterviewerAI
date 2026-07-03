"""
-------------------------------------------------------
Interview Services
-------------------------------------------------------
"""

from app.interview.generator import generate_questions
from app.interview.prompts import (
    build_candidate_profile,
    build_question_prompt,
)

from app.extensions import db
from app.models.interview import Interview
from app.models.question import InterviewQuestion
from app.models.resume import Resume


def save_questions(interview, questions):

    for item in questions["questions"]:

        question = InterviewQuestion(
            interview_id=interview.id,
            question_number=item["number"],
            category=item["category"],
            question_text=item["question"]
        )

        db.session.add(question)

    db.session.commit()


def create_interview(user_id):

    resume = (
        Resume.query
        .filter_by(user_id=user_id)
        .order_by(Resume.id.desc())
        .first()
    )

    if resume is None:
        return None

    interview = Interview(
        resume_id=resume.id,
        user_id=user_id,
        target_job=resume.target_job,
        experience_level=resume.experience_level,
        status="GENERATING"
    )

    db.session.add(interview)
    db.session.commit()

    candidate_profile = build_candidate_profile(
        resume.extracted_text,
        resume.target_job,
        resume.experience_level,
    )

    prompt = build_question_prompt(candidate_profile)

    response = generate_questions(prompt)

    save_questions(interview, response)

    interview.status = "READY"

    db.session.commit()

    return interview