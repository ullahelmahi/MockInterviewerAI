"""
-------------------------------------------------------
Resume Upload Services
-------------------------------------------------------
"""

from pathlib import Path
from uuid import uuid4

from flask import current_app
from flask_login import current_user
from werkzeug.utils import secure_filename

from app.extensions import db
from app.models.resume import Resume
from app.utils.pdf import extract_text_from_pdf


def save_resume(
    file,
    target_job,
    experience_level
):
    """
    Save an uploaded resume to disk and database.
    """

    upload_folder = (
        Path(current_app.root_path).parent
        / "uploads"
        / "resumes"
    )

    upload_folder.mkdir(parents=True, exist_ok=True)

    original_filename = secure_filename(file.filename)

    extension = Path(original_filename).suffix

    unique_filename = f"{uuid4().hex}{extension}"

    filepath = upload_folder / unique_filename

    file.save(filepath)

    resume = Resume(
        filename=unique_filename,
        original_filename=original_filename,
        target_job=target_job,
        experience_level=experience_level,
        extracted_text=extract_text_from_pdf(str(filepath)),
        user_id=current_user.id
    )

    db.session.add(resume)
    db.session.commit()

    return resume