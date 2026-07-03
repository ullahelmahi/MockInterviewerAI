"""
-------------------------------------------------------
Gemini AI Evaluation
-------------------------------------------------------
"""

import json

from google import genai

from config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


def evaluate_answer(question, transcript):

    prompt = f"""
You are a professional interview evaluator.

Evaluate the candidate's answer.

Interview Question:
{question}

Candidate Answer:
{transcript}

Return ONLY valid JSON.

Format:

{{
    "score": 8.5,
    "strengths": [
        "...",
        "..."
    ],
    "weaknesses": [
        "...",
        "..."
    ],
    "feedback": "..."
}}

Do not return markdown.
Do not use ```json.
Return JSON only.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()

    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    start = text.find("{")
    end = text.rfind("}")

    text = text[start:end + 1]

    try:
        return json.loads(text)

    except Exception as e:

        print("=" * 60)
        print("INVALID GEMINI RESPONSE")
        print(text)
        print("=" * 60)

        raise e


def evaluate_interview(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a senior HR interviewer with over 15 years of experience.

Evaluate the COMPLETE interview.

Evaluate the candidate in the following categories.

1. Overall Score (0-100)
2. Technical Skills (0-100)
3. Communication Skills (0-100)
4. Behavioral Skills (0-100)

You MUST also provide:

1. At least 3 strengths.
2. At least 5 weaknesses.
3. At least 5 recommendations.
4. A hiring recommendation.

Even if the interview performance is poor,
identify positive qualities whenever possible.

Possible strengths include:

- Professional attitude
- Politeness
- Communication attempt
- Confidence
- Willingness to learn
- Relevant education
- Good motivation
- Positive personality
- Problem solving
- Teamwork

Never return an empty strengths list.

Return ONLY valid JSON.

Format:

{{
    "overall_score": 85,
    "technical_score": 82,
    "communication_score": 88,
    "behavioral_score": 84,
    "strengths": [
        "...",
        "...",
        "..."
    ],
    "weaknesses": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ],
    "recommendations": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ],
    "hiring_recommendation": "Hire"
}}

Do not return markdown.
Do not return explanations.
Return JSON only.

Interview:

{prompt}
"""
    )

    text = response.text.strip()

    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()

    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    start = text.find("{")
    end = text.rfind("}")

    text = text[start:end + 1]

    try:
        return json.loads(text)

    except Exception as e:

        print("=" * 60)
        print("INVALID GEMINI RESPONSE")
        print(text)
        print("=" * 60)

        raise e