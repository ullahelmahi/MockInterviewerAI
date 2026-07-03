from flask import render_template
from flask_login import login_required, current_user

from app.interview_session import interview_session

from app.models.interview import Interview
from app.models.question import InterviewQuestion


@interview_session.route("/<int:interview_id>")
@login_required
def interview(interview_id):

    interview = Interview.query.filter_by(
        id=interview_id,
        user_id=current_user.id
    ).first_or_404()

    questions = (
        InterviewQuestion.query
        .filter_by(interview_id=interview.id)
        .order_by(InterviewQuestion.question_number)
        .all()
    )

    return render_template(
        "interview/interview.html",
        interview=interview,
        questions=questions
    )