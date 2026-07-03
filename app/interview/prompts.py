"""
-------------------------------------------------------
Interview Prompt Builder
-------------------------------------------------------
Purpose:
Contains all prompt templates used by Gemini AI.
-------------------------------------------------------
"""


def build_candidate_profile(
    resume_text: str,
    target_job: str,
    experience_level: str
) -> str:
    """
    Build a structured candidate profile from the uploaded resume.
    """

    return f"""
Candidate Resume

{resume_text}

Target Job

{target_job}

Experience Level

{experience_level}
"""


def build_question_prompt(candidate_profile: str) -> str:
    """
    Build the prompt for interview question generation.
    """

    return f"""
You are a Senior Technical Interviewer with more than 15 years of interviewing experience at multinational companies.

Conduct a realistic mock interview.

Candidate Profile

{candidate_profile}

Interview Rules

- Generate EXACTLY 9 interview questions.

Question Distribution

1. Self Introduction

2. Resume-based question

3. Technical

4. Technical

5. Technical

6. Technical

7. Technical

8. HR / Behavioural

9. HR / Behavioural

Additional Rules

- Match the difficulty with the candidate's experience level.
- Technical questions must match the target job.
- Resume question must only use information found in the resume.
- HR questions should evaluate communication and professionalism.
- Do not repeat questions.
- Do not explain anything.

Return ONLY valid JSON.

Example

{{
    "questions":[
        {{
            "number":1,
            "category":"Introduction",
            "question":"Tell me about yourself."
        }}
    ]
}}
"""