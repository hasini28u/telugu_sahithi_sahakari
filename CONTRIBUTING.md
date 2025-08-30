# Contributing to తెలుగు సాహితీ సహకారి (Telugu Sahiti Sahakari)

First off, thank you for considering contributing to Telugu Sahiti Sahakari! Your support is essential to our mission of preserving and promoting Telugu literary heritage through community-powered digitization and AI. Every contribution—big or small—brings us closer to building an open, accessible digital corpus for Telugu language research.

---

## Code of Conduct

To foster a respectful, welcoming, and inclusive environment, we expect all participants in this project to adhere to our Code of Conduct.  
Please take a moment to review it before getting started. Mutual respect is the foundation of our community.

---

## How You Can Contribute

There are several valuable ways you can help the Telugu Sahiti Sahakari project:

### 1. Reporting Bugs or Suggesting Features

- **Report bugs:** Clearly describe the issue, provide steps to reproduce, and detail expected vs. actual behavior.
- **Suggest features:** Outline your idea, the problem it solves, and how it can benefit users.
- Please use the respective **Bug Report** or **Feature Request** templates when creating issues in [our repository](https://code.swecha.org/ananyakrishna/telugu_sahithi_sahakaari.git).

---

### 2. Data Contributions (Most Important!)

Data is the cornerstone of the Telugu Sahiti Sahakari project!  
The best way to contribute is by uploading Telugu literary works—books, poems, clippings, and handwritten notes—through the application interface.

#### Data Quality Guidelines
- **Accuracy:** Upload only genuine Telugu literature with correct titles and, if possible, author information.
- **Consent:** If your uploads contain media with identifiable people, obtain their permission prior to submission.
- **Clarity:** Add concise, clear descriptions/titles so material is usable for research and readers alike.
- **Privacy:** Avoid uploading any sensitive or personal data unrelated to literature.

---

### 3. Code Contributions

We welcome contributors of all skill levels! To contribute code:

### Fork & Clone git clone
https://code.swecha.org/ananyakrishna/telugu_sahithi_sahakaari.git cd
telugu_sahithi_sahakaari

text \#### Create a New Branch For a new feature: git checkout -b
feature/your-feature-name

text For a bug fix: git checkout -b fix/your-bug-description

text \#### Make Your Changes & Commit Follow conventional commit
messages. Example: new feature git commit -m "feat: Add language
switcher to upload interface"

Example: bug fix git commit -m "fix: Handle network errors gracefully on
file upload"

text \#### Push & Open a Merge Request (MR) git push origin
feature/your-feature-name

text Then, open a **Merge Request** into the main branch via the Swecha
GitLab interface.\
Please fill in the MR template with clear explanations and testing
instructions.

------------------------------------------------------------------------

## Development Setup

#### Prerequisites

-   Python 3.8+
-   Git
-   Swecha Corpus Platform account (for API testing and category
    uploads)

#### Installation

Clone the repo: git clone
https://code.swecha.org/ananyakrishna/telugu_sahithi_sahakaari.git cd
telugu_sahithi_sahakaari

text Create a virtual environment and activate it: python3 -m venv .venv
source .venv/bin/activate \# On Windows:
.venv`\Scripts`{=tex}`\activate`{=tex}

text Install dependencies: pip install -r requirements.txt

text

------------------------------------------------------------------------

### Running the Application

For the backend (FastAPI): uvicorn backend.core.main:app --reload

For the frontend (Streamlit): streamlit run backend/frontend/app.py

text Open your browser at: <http://localhost:8501>

------------------------------------------------------------------------

## Getting Help

If you have any questions or need assistance: - Open an Issue in [our
repository](https://code.swecha.org/ananyakrishna/telugu_sahithi_sahakaari.git) -
Contact the project maintainer via email: \[your-email@example.com\]
(replace with maintainer email)

------------------------------------------------------------------------

## Thank You!

Your effort to preserve and promote Telugu literature is highly valued.\
Together, we can build a unique open archive and inspire future
generations!

*Telugu Sahiti Sahakari Team*
