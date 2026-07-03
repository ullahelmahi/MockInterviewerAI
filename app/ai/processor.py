"""
-------------------------------------------------------
AI Processing Pipeline
-------------------------------------------------------
"""

from pathlib import Path

from flask import current_app

from app.ai.whisper import transcribe_video
from app.ai.gemini import evaluate_answer
from app.ai.voice import analyze_voice
from app.ai.face import analyze_face
from app.extensions import db


def process_answer(answer):

    print("=" * 60)
    print("AI PROCESSING STARTED")
    print("=" * 60)

    video_path = (
        Path(current_app.config["UPLOAD_FOLDER"])
        / answer.video_path
    )

    # -----------------------------------
    # Whisper
    # -----------------------------------

    transcript = transcribe_video(
        str(video_path)
    )

    answer.transcript = transcript

    print("\nTranscript")
    print(transcript)

    # -----------------------------------
    # Gemini
    # -----------------------------------

    gemini_result = evaluate_answer(
        answer.question.question_text,
        transcript
    )

    print("\nGemini Result")
    print(gemini_result)

    # -----------------------------------
    # Voice Analysis
    # -----------------------------------

    voice_result = analyze_voice(
        transcript,
        duration_seconds=answer.duration or 60
    )

    print("\nVoice Analysis")
    print(voice_result)

    # -----------------------------------
    # Face Analysis
    # -----------------------------------

    face_result = analyze_face(
        str(video_path)
    )

    # -----------------------------------
    # Save AI Results
    # -----------------------------------

    answer.gemini_score = gemini_result.get("score")
    answer.gemini_feedback = gemini_result.get("feedback")

    answer.speech_rate = voice_result["words_per_minute"]
    answer.filler_words = voice_result["filler_words"]
    answer.voice_score = voice_result["voice_score"]
    answer.voice_pace = voice_result["pace"]
    answer.voice_fluency = voice_result["fluency"]

    answer.eye_contact_score = face_result.get("eye_contact")
    answer.face_detection = face_result.get("face_percentage")

    answer.status = "COMPLETED"

    db.session.commit()

    print("\nFace Analysis")
    print(face_result)

    print("=" * 60)
    print("AI PROCESSING COMPLETE")
    print("=" * 60)

    return answer