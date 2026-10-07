import streamlit as st

st.title("🤖 AI Resume Analyzer")

st.write("Upload your resume and get a basic analysis.")

resume = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "txt"]
)

if resume:
    st.success("Resume uploaded successfully! ✅")

    st.subheader("Resume Details")
    st.write("File name:", resume.name)

    st.info("AI analysis will be added in the next version.")

st.divider()

st.caption("AI Resume Analyzer | B.Tech AI Project")
