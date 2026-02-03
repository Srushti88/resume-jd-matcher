Resume ↔ Job Description Matcher

Overview

This project compares a candidate’s resume with a job description and produces:
-Match Score
-Analysis with strengths, gaps, and improvement suggestions


Setup Instructions
1) Create .env
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key

2) Install requirements
pip install -r requirements.txt

3) Run Backend
uvicorn app.main:app --reload

4) Run UI (new terminal)
streamlit run ui/streamlit_app.py



Sample Usage

- Upload any resume PDF
- Paste any job description
- Select Groq or Gemini
- Get score and analysis



Author: Srushti Vispute