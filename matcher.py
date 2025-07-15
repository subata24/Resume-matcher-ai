from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def extract_resume_keywords(resume_text):
    resume_text = resume_text.lower()
    tokens = word_tokenize(resume_text)

    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    keywords = [
        word for word in tokens
        if word not in stop_words and word not in punctuation and word.isalpha()
    ]

    return set(keywords)

def calculate_match(resume_text, job_keywords):
    resume_keywords = extract_resume_keywords(resume_text)

    job_keywords_set = set(job_keywords)

    matched_keywords = resume_keywords.intersection(job_keywords_set)
    missing_keywords = job_keywords_set - resume_keywords

    match_score = round((len(matched_keywords) / len(job_keywords_set)) * 100, 2) if job_keywords_set else 0
 

    print("\n[DEBUG] Resume Keywords:")
    print(resume_keywords)

    print("\n[DEBUG] Job Keywords:")
    print(job_keywords_set)

    print("\n[DEBUG] Matched:")
    print(matched_keywords)

    print("\n[DEBUG] Missing:")
    print(missing_keywords)

    print("Resume Keywords Count:", len(resume_keywords))
    print("Job Keywords Count:", len(job_keywords_set))

    return {
        "match_score": match_score,
        "matched_keywords": list(matched_keywords),
        "missing_keywords": list(missing_keywords)
    }
