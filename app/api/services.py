from pathlib import Path
from flask import ( jsonify, request, current_app,)
from app.extensions import db
from app.models.answer import InterviewAnswer
from app.models.question import InterviewQuestion
from app.ai.processor import process_answer


def save_video( video,interview_id,question_number):

    upload_folder = (
        Path(current_app.config["UPLOAD_FOLDER"])
        / "interviews"
        / f"interview_{interview_id}"
    )

    upload_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = f"q{question_number}.webm"

    file_path = upload_folder / filename

    video.save(file_path)

    print("=" * 60)
    print("VIDEO SAVED")
    print(file_path)
    print("=" * 60)

    return file_path

def save_answer(
    interview_id,
    question_number,
    video_path ):

    question = InterviewQuestion.query.filter_by(
        interview_id=interview_id,
        question_number=question_number
    ).first()

    if not question:

        return

    answer = InterviewAnswer.query.filter_by(
        interview_id=interview_id,
        question_id=question.id
    ).first()

    if not answer:

        answer = InterviewAnswer(

            interview_id=interview_id,

            question_id=question.id

        )

        db.session.add(answer)

    answer.video_path = ( f"interviews/interview_{interview_id}/q{question_number}.webm")

    answer.status = "VIDEO_UPLOADED"

    db.session.commit()

    return answer , question


def upload_answer():

    video = request.files.get("video")

    interview_id = request.form.get("interview_id")

    question_number = request.form.get("question_number")

    if not video:

        return jsonify({

            "success": False,

            "message": "No video uploaded."

        }), 400
    
    file_path = save_video(
        video,
        interview_id,
        question_number
    )

    answer, _ = save_answer(
        interview_id,
        question_number,
        file_path
    )

    process_answer(answer)

    db.session.commit()
    return jsonify({

        "success": True

    })