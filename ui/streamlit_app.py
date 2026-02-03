import streamlit as st
import requests

st.title("Resume vs Job Description Matcher")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description
jd_text = st.text_area("Paste Job Description here")

# Model Selection
model_name = st.selectbox("Choose LLM Model", ["groq", "gemini"])

if st.button("Analyze"):
    if resume_file and jd_text:

        files = {
            "resume": (resume_file.name, resume_file, "application/pdf")
        }

        data = {
            "jd_text": jd_text,
            "model_name": model_name
        }

        try:
            response = requests.post(
                "http://localhost:8000/analyze",
                files=files,
                data=data,
                timeout=60
            )

            # Check if backend responded correctly
            if response.status_code == 200:
                try:
                    result = response.json()

                    st.subheader("Match Score")
                    st.write(result["match_score"])

                    st.subheader("Analysis")
                    st.write(result["analysis"])

                except Exception:
                    st.error("Backend returned invalid JSON.")
                    st.text(response.text)

            else:
                st.error(f"Backend Error ({response.status_code})")
                st.text(response.text)

        except requests.exceptions.RequestException as e:
            st.error("Could not connect to backend. Make sure FastAPI is running.")
            st.text(str(e))

    else:
        st.warning("Please upload resume and enter job description.")
