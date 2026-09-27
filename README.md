# 🔀 Professional Git Tracker

> Turn raw code changes into professional commit messages and plain-English progress reports — powered by Google Gemini AI.

---

## What It Does

**Professional Git Tracker** is a Streamlit web application that helps developers — especially those learning Git — communicate their code changes more effectively.

You paste a code diff or snippet into the app, click a button, and the app uses the **Google Gemini API** to:

1. **Generate a professional Git commit message** suitable for use in a real repository.
2. **Explain the code changes in plain English**, acting as a mentor walking you through what was done and why.

It's designed to bridge the gap between writing code and clearly documenting it for version control and collaboration.

---

## Screenshots

> _Add a screenshot of the running app here (e.g. `docs/screenshot.png`)._

---

## Prerequisites

Before running this project, make sure you have the following installed:

| Requirement | Version |
|---|---|
| [Python](https://www.python.org/downloads/) | 3.8 or higher |
| [pip](https://pip.pypa.io/en/stable/) | Latest recommended |

You will also need a **Google Gemini API key**:

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Create a new API key.
3. Copy the key — you will paste it into `app.py` in the setup step below.

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/git-tracker-app.git
cd git-tracker-app
```

### 2. Create and activate a virtual environment (recommended)

```bash
# Create the environment
python -m venv venv

# Activate it — Linux / macOS
source venv/bin/activate

# Activate it — Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Open `app.py` and replace the placeholder value on line 24 with your real API key:

```python
api_key = "YOUR_GEMINI_API_KEY_HERE"
```

> ⚠️ **Security note:** Never commit a real API key to a public repository. Consider loading it from an environment variable or a `.env` file (e.g. with `python-dotenv`) before publishing.

---

## Running the App

```bash
streamlit run app.py
```

Streamlit will print a local URL (typically `http://localhost:8501`). Open it in your browser.

---

## Usage

1. Paste your code changes or a `git diff` snippet into the text area.
2. Click **"Generate Commit & Report"**.
3. The app will call the Gemini API and display:
   - A professional commit message.
   - A plain-English explanation of your changes.

---

## Project Structure

```
git-tracker-app/
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## License

This project is open source. Add your preferred license here (e.g. MIT).
# professional-git-tracker
