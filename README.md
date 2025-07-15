# 📄 Resume Matcher AI

A smart NLP-powered tool that compares your resume to a job description and shows how well they match — with keyword highlights, match score, and feedback.

🚀 **Live Demo:**  
👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Subata24/Resume-matcher-ai)

---

## 💡 What It Does

- 📤 Upload your **Resume (PDF)** and **Job Description (TXT)**
- 🧠 Uses **Natural Language Processing** (NLTK + PyMuPDF) to extract keywords
- 📊 Calculates a **Match Score**
- ✅ Shows **Matched Keywords**
- ❌ Lists **Missing Keywords**

---

## 🛠️ Technologies Used

- Python 🐍  
- [Gradio](https://www.gradio.app/) for the interactive web interface  
- [NLTK](https://www.nltk.org/) for NLP (tokenizing, stopwords)  
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) for reading PDF resumes  
- Hugging Face Spaces for free deployment

---

## 📦 Installation (for local run)

```bash
git clone https://github.com/subata24/Resume-matcher-ai.git
cd Resume-matcher-ai
pip install -r requirements.txt
python app.py


## Features

- Upload Resume (PDF) + Job Description (TXT)
- NLP-based keyword extraction
- Match Score, Matched & Missing Keywords

## Tech Stack

- Python, Gradio
- NLTK, PyMuPDF
- Hosted on Hugging Face Spaces
