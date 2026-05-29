import streamlit as st
import pandas as pd

from src.resume_parser import extract_text
from src.utils import clean_text
from src.screening import rank_resumes

st.title("AI Resume Screening System")

job_description = st.text_area(
    "Enter Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Screen Resumes"):

    if uploaded_files and job_description:

        resumes = []
        candidate_names = []

        for file in uploaded_files:

            text = extract_text(file)

            cleaned_resume = clean_text(text)

            resumes.append(cleaned_resume)

            candidate_names.append(file.name)

        cleaned_jd = clean_text(job_description)

        scores = rank_resumes(
            cleaned_jd,
            resumes
        )

        results = []

        for i in range(len(candidate_names)):

            results.append({
                "Candidate": candidate_names[i],
                "Match Score": round(scores[i] * 100, 2)
            })

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Match Score",
            ascending=False
        )

        st.success("Screening Completed")

        st.dataframe(df)

    else:
        st.warning("Please upload resumes and enter job description.")
