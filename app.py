import gradio as gr
import fitz  # PyMuPDF
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# Download necessary NLTK data
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# ✅ Extract resume text
def extract_resume_text(resume_path):
    text = ""
    with fitz.open(resume_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# ✅ Extract job description keywords
def extract_job_keywords(job_path):
    with open(job_path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    punctuation = set(string.punctuation)
    keywords = [word for word in tokens if word not in stop_words and word.isalpha() and word not in punctuation]
    return set(keywords)

# ✅ Match logic
def calculate_match(resume_text, job_keywords):
    resume_text = resume_text.lower()
    resume_tokens = word_tokenize(resume_text)
    resume_keywords = set([
        word for word in resume_tokens
        if word not in stopwords.words("english") and word.isalpha()
    ])
    matched = resume_keywords & job_keywords
    match_score = round((len(matched) / len(job_keywords)) * 100, 2) if job_keywords else 0
    missing = job_keywords - resume_keywords
    return match_score, list(matched), list(missing)

# ✅ Main Gradio function
def match_resume(resume_file, job_file):
    try:
        resume_text = extract_resume_text(resume_file.name)
        job_keywords = extract_job_keywords(job_file.name)
        match_score, matched, missing = calculate_match(resume_text, job_keywords)

        return f"✅ Match Score: {match_score}%", ", ".join(matched), ", ".join(missing)
    except Exception as e:
        return f"❌ Error: {str(e)}", "", ""

# ✅ Gradio UI
iface = gr.Interface(
    fn=match_resume,
    inputs=[
        gr.File(label="Upload Resume (PDF)", file_types=[".pdf"]),
        gr.File(label="Upload Job Description (TXT)", file_types=[".txt"])
    ],
    outputs=[
        gr.Textbox(label="Match Score"),
        gr.Textbox(label="Matched Keywords"),
        gr.Textbox(label="Missing Keywords")
    ],
    title="📄 Resume Matcher AI",
    description="Upload your Resume and Job Description to see how well they match. Built with NLP + Python 💻"
)

if __name__ == "__main__":
    iface.launch()