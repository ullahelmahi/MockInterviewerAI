"""
-------------------------------------------------------
Cleanup Utility
-------------------------------------------------------
Deletes temporary interview files after report generation.
-------------------------------------------------------
"""

import shutil
from pathlib import Path


UPLOAD_FOLDER = Path("uploads")


def delete_file(file_path: Path):

    try:

        if file_path.exists():

            file_path.unlink()

            print(f"Deleted: {file_path}")

    except Exception as e:

        print(f"Cannot delete {file_path}")
        print(e)


def delete_folder(folder: Path):

    try:

        if folder.exists():

            shutil.rmtree(folder)

            print(f"Deleted Folder: {folder}")

    except Exception as e:

        print(f"Cannot delete folder {folder}")
        print(e)


def cleanup_interview(interview_id):
    """
    Removes every temporary file created during interview processing.
    """

    interview_folder = (
        UPLOAD_FOLDER /
        "interviews" /
        f"interview_{interview_id}"
    )

    print("=" * 60)
    print("STARTING CLEANUP")
    print("=" * 60)

    # -------------------------------------
    # Delete interview media folder
    # -------------------------------------

    delete_folder(interview_folder)

    # -------------------------------------
    # Delete loose temporary files
    # -------------------------------------

    temp_extensions = [
        "*.wav",
        "*.webm",
        "*.mp3",
        "*.aac",
        "*.jpg",
        "*.jpeg",
        "*.png",
        "*.txt"
    ]

    for extension in temp_extensions:

        for file in UPLOAD_FOLDER.rglob(extension):

            delete_file(file)

    print("=" * 60)
    print("CLEANUP COMPLETE")
    print("=" * 60)