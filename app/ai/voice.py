import re

FILLER_WORDS = {
    "um",
    "uh",
    "hmm",
    "like",
    "actually",
    "basically",
    "well",
    "so"
}


def analyze_voice(transcript, duration_seconds):

    transcript = transcript.strip()

    words = re.findall(r"\b[\w']+\b", transcript.lower())

    total_words = len(words)

    duration_minutes = max(duration_seconds / 60, 0.01)

    words_per_minute = round(
        total_words / duration_minutes,
        1
    )

    filler_count = sum(
        1 for word in words
        if word in FILLER_WORDS
    )

    # ------------------------
    # Speaking Pace
    # ------------------------

    if 100 <= words_per_minute <= 160:
        pace = "Good"
        pace_score = 40

    elif 80 <= words_per_minute < 100:
        pace = "Moderate"
        pace_score = 30

    elif 60 <= words_per_minute < 80:
        pace = "Slow"
        pace_score = 20

    else:
        pace = "Very Slow" if words_per_minute < 60 else "Fast"
        pace_score = 10

    # ------------------------
    # Filler Words
    # ------------------------

    if filler_count == 0:
        filler_score = 30

    elif filler_count <= 2:
        filler_score = 25

    elif filler_count <= 5:
        filler_score = 15

    else:
        filler_score = 5

    # ------------------------
    # Transcript Length
    # ------------------------

    if total_words >= 150:
        length_score = 30

    elif total_words >= 100:
        length_score = 25

    elif total_words >= 50:
        length_score = 15

    else:
        length_score = 5

    # ------------------------
    # Final Voice Score
    # ------------------------

    voice_score = pace_score + filler_score + length_score

    if voice_score >= 85:
        fluency = "Excellent"

    elif voice_score >= 70:
        fluency = "Good"

    elif voice_score >= 50:
        fluency = "Average"

    else:
        fluency = "Needs Improvement"

    return {

        "total_words": total_words,

        "duration_seconds": duration_seconds,

        "words_per_minute": words_per_minute,

        "filler_words": filler_count,

        "pace": pace,

        "voice_score": voice_score,

        "fluency": fluency

    }