"""
-------------------------------------------------------
Whisper AI Service
-------------------------------------------------------
Speech-to-Text using Faster-Whisper
-------------------------------------------------------
"""

from faster_whisper import WhisperModel


# Load model only once
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def transcribe_video(video_path):

    segments, info = model.transcribe(video_path)

    transcript = ""

    for segment in segments:

        transcript += segment.text + " "

    return transcript.strip()