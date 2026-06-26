from fpdf import FPDF
from PyPDF2 import PdfReader
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="📚 SmartStudy AI",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Settings")

difficulty = st.sidebar.selectbox(
    "Quiz Difficulty",
    ["Easy", "Medium", "Hard"]
)

# -----------------------------
# Title
# -----------------------------
st.title("📚 SmartStudy AI")
st.caption("AI-Powered Study Assistant")
st.markdown("---")

# -----------------------------
# PDF Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

notes = ""

if uploaded_file:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()

        if text:
            notes += text + "\n"

# -----------------------------
# Manual Notes
# -----------------------------
manual_notes = st.text_area(
    "Or Paste Notes Here",
    height=250
)

if manual_notes:
    notes = manual_notes

st.markdown("---")

# -----------------------------
# Buttons in One Row
# -----------------------------
col1, col2, col3 = st.columns(3)

# =====================================================
# Generate Notes
# =====================================================
with col1:

    if st.button("📚 Generate Notes"):

        if notes:

            prompt = f"""
You are an expert teacher.

Analyze these notes and generate:

1. Detailed Summary

2. Key Points

3. Important Exam Questions

4. 5 {difficulty} Quiz Questions

Notes:

{notes}
"""

            response = model.generate_content(prompt)

            st.subheader("📚 Generated Notes")

            st.markdown(response.text)

            result = response.text

        else:
            st.warning("Please upload or enter notes.")

# =====================================================
# Flashcards
# =====================================================
with col2:

    if st.button("📝 Generate Flashcards"):

        if notes:

            prompt = f"""
Create 10 study flashcards.

Format:

Question:
Answer:

Notes:

{notes}
"""

            response = model.generate_content(prompt)

            st.subheader("📖 Flashcards")

            st.markdown(response.text)

            result = response.text

        else:
            st.warning("Please upload or enter notes.")

# =====================================================
# Study Time
# =====================================================
with col3:

    if st.button("⏰ Study Time"):

        if notes:

            prompt = f"""
Estimate the study time required for these notes.

Provide:

• Beginner

• Intermediate

• Advanced

Also provide study tips.

Notes:

{notes}
"""

            response = model.generate_content(prompt)

            st.subheader("⏰ Study Time")

            st.markdown(response.text)

            result = response.text

        else:
            st.warning("Please upload or enter notes.")

# -----------------------------
# PDF Download
# -----------------------------
if "result" in locals():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    text = result.encode("latin-1", "replace").decode("latin-1")

    pdf.multi_cell(0, 10, text)

    pdf.output("StudyNotes.pdf")

    with open("StudyNotes.pdf", "rb") as file:

        st.download_button(
            "📥 Download PDF",
            data=file,
            file_name="StudyNotes.pdf",
            mime="application/pdf"
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption("🚀 Built with Streamlit + Gemini 2.5 Flash")