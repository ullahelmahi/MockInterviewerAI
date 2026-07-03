from app.api import api

from app.api.services import upload_answer


@api.route(
    "/upload-answer",
    methods=["POST"]
)
def upload_answer_route():

    return upload_answer()