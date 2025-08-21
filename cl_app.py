import google.generativeai as genai
import streamlit as st
genai.configure(api_key=st.secrets["my_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="Cover Letter Generator by Saptarshi", page_icon="📝", layout="centered")
st.subheader("Generate a tailored, professional cover letter in seconds using AI.")
with st.expander("📋 Fill in Your Details", expanded=True):
    job_title = st.text_input("Job Title")
    company_name=st.text_input("Name of the company where you are applying for:")
    resume_summary = st.text_area("Resume Summary / Highlights", height=150)
    highest_education = st.text_input("Highest Academic Qualification with Specialization")
    experience = st.selectbox("Experience Level", ["Fresher", "1-3 years of experience", "3+ years of experience"])
if st.button("Generate Your Cover Letter"):
    if job_title and resume_summary and highest_education and experience:
        with st.spinner("_Crafting your personalized cover letter......_"):
            prompt = f"""
            Write a professional cover letter for the position of {job_title}.
            For the company {company_name} then
            use the resume summary: {resume_summary}.
            The candidate's highest qualification is {highest_education},
            and the experience level is {experience}.
            Make it concise, professional, and tailored to the role.
            """
            response = model.generate_content(prompt)
            cover_letter = response.text

        st.success("Cover Letter Generated Successfully!🤗")
        st.markdown("Your Cover Letter is as following")
        st.write(cover_letter)
    else:
        st.error("Please fill out all fields before generating the cover letter.⚠️")
