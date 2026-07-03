from app.models.resume import Resume
from app.models.interview import Interview


def get_latest_resume(user_id):

    return (
        Resume.query
        .filter_by(user_id=user_id)
        .order_by(Resume.id.desc())
        .first()
    )


def get_user_interviews(user_id):

    return (
        Interview.query
        .filter_by(user_id=user_id)
        .order_by(Interview.id.desc())
        .all()
    )