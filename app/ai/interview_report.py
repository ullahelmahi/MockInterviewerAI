"""
-------------------------------------------------------
Interview Report Generator
-------------------------------------------------------
"""

from app.models.interview import Interview
from app.models.question import InterviewQuestion
from app.models.answer import InterviewAnswer
from app.models.report import InterviewReport


def load_interview(interview_id):

    interview = Interview.query.get(interview_id)

    questions = (
        InterviewQuestion.query
        .filter_by(interview_id=interview_id)
        .order_by(InterviewQuestion.question_number)
        .all()
    )

    answers = (
        InterviewAnswer.query
        .join(
            InterviewQuestion,
            InterviewAnswer.question_id == InterviewQuestion.id
        )
        .filter(
            InterviewQuestion.interview_id == interview_id
        )
        .order_by(
            InterviewQuestion.question_number
        )
        .all()
    )

    return interview, questions, answers


def build_prompt(
    interview,
    questions,
    answers
):

    prompt = f"""
You are a professional senior interviewer.

Evaluate the COMPLETE interview.

Target Job:
{interview.target_job}

Experience Level:
{interview.experience_level}

----------------------------------------
INTERVIEW
----------------------------------------

"""

    for question, answer in zip(questions, answers):

        transcript = answer.transcript

        if not transcript:

            transcript = "No Answer"

        prompt += f"""

Question {question.question_number}

Category:
{question.category}

Question:
{question.question_text}

Candidate Answer:
{transcript}

----------------------------------------

"""

    return prompt