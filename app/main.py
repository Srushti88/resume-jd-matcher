from fastapi import FastAPI, UploadFile, File, Form
from app.services.parser import ResumeParser
from app.services.matcher import ResumeJDMatcher
from app.core.prompts import build_analysis_prompt
from app.models.schemas import AnalysisResponse

from app.services.llm.groq_llm import GroqLLM
from app.services.llm.gemini_llm import GeminiLLM

app = FastAPI()

parser = ResumeParser()
matcher = ResumeJDMatcher()


def get_llm(model_name: str):
    if model_name == "groq":
        return GroqLLM()
    elif model_name == "gemini":
        return GeminiLLM()
    else:
        raise ValueError("Invalid model selected")


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    resume: UploadFile = File(...),
    jd_text: str = Form(...),
    model_name: str = Form(...)
):
    
    file_path = f"temp_{resume.filename}"
    with open(file_path, "wb") as f:
        f.write(await resume.read())

    # Extract resume text
    resume_text = parser.extract_text_from_pdf(file_path)

    # Calculate match score
    score = matcher.calculate_match(resume_text, jd_text)

    # Build prompt
    prompt = build_analysis_prompt(resume_text, jd_text, score)

    # Select LLM
    llm = get_llm(model_name)
    explanation = llm.generate(prompt)

    return AnalysisResponse(
        match_score=score,
        analysis=explanation
    )
