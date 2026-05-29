# AI Resume Screening System

## Project Overview

The AI Resume Screening System is a Machine Learning and NLP-based application that automatically screens and ranks resumes based on a given job description.

The system extracts text from uploaded resumes, processes the content using Natural Language Processing (NLP), and calculates similarity scores between resumes and job descriptions using TF-IDF and Cosine Similarity.

---

# Features

* Upload multiple resumes in PDF format
* Extract resume text automatically
* Enter job description
* AI-based resume ranking
* Match score calculation
* Interactive Streamlit dashboard
* NLP text preprocessing

---

# Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK
* Pandas
* PyPDF2

---

# Project Structure

```bash
RESUME_SCREENING/
│
├── app.py
├── setup.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── screening.py
│   └── utils.py
│
└── resumes/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/resume-screening.git
```

## Move to Project Folder

```bash
cd resume-screening
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# How It Works

1. Upload resumes in PDF format
2. Enter the job description
3. System extracts resume text
4. NLP preprocessing is applied
5. TF-IDF vectorization converts text into numerical vectors
6. Cosine similarity calculates matching scores
7. Candidates are ranked automatically

---

# Machine Learning Concepts Used

## TF-IDF

TF-IDF measures the importance of words in a document.

TF-IDF Formula:

```text
TF-IDF(t,d) = TF(t,d) × log(N / DF(t))
```

## Cosine Similarity

Cosine similarity measures similarity between two vectors.

Formula:

```text
cos(θ) = (A · B) / (||A|| ||B||)
```

---

# Example Output

| Candidate | Match Score |
| --------- | ----------- |
| John.pdf  | 89.5%       |
| Alice.pdf | 82.1%       |
| Mike.pdf  | 75.3%       |

---

# Future Improvements

* BERT Embeddings
* Resume Skill Extraction
* OCR Support for Scanned Resumes
* Candidate Recommendation System
* Login Authentication
* Database Integration
* Cloud Deployment

---

# Skills Covered

* Machine Learning
* Natural Language Processing (NLP)
* Python Development
* Streamlit
* Data Processing
* Cosine Similarity
* TF-IDF

---

# Use Cases

* HR Resume Screening
* Automated Candidate Ranking
* Recruitment Systems
* AI-based Hiring Solutions

---

# Author

Bhagyashri Patil

---

# License

This project is open-source and available under the MIT License.
