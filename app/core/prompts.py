def build_analysis_prompt(resume_text: str, jd_text: str, score: int) -> str:
    prompt = f"""
You are an expert technical recruiter.

A resume has been compared with a job description and received a match score of {score}%.

STRICT RULES:
- Maximum 3 bullet points per section
- Each point must be single short sentence
- Single line response for each point
- No repetition
- No extra headings
- Follow the exact format below

FORMAT:

Positive Points:
- point
- point
- point

Negative Points:
- point
- point
- point

Suggestions:
- point
- point
- point

Mistakes to Avoid:
- point
- point
- point

Resume:
{resume_text}

Job Description:
{jd_text}
"""
    return prompt
