# 🎯 Career Copilot

**Career Copilot** is a Streamlit-based career preparation assistant designed to help students prepare for their desired career path.

The application provides features for **resume analysis, skill-gap identification, interview practice, and personalized learning roadmaps** through a simple and interactive dashboard.

---

## 🚀 Features

### 📊 Dashboard

The Career Copilot dashboard provides an overview of the user's career preparation, including:

* 📄 Resume Score
* 🎯 Skill Match
* 🎤 Interview Score
* 🚀 Career Readiness
* Quick access to career preparation modules

### 📄 Resume Analyzer

The Resume Analyzer allows users to upload their resume in:

* PDF
* DOCX
* TXT

It provides a quick overview of:

* Resume score
* ATS compatibility
* Profile strength
* Resume strengths
* Improvement suggestions
* Target-role recommendations

> **Note:** The current version uses demo evaluation values. Actual automated resume parsing and AI-based scoring can be added in future versions.

### 🎯 Skill Gap Analysis

The Skill Gap module compares a student's current skills with the skills commonly required for a selected career role.

Supported career paths include:

* Python Developer
* Java Developer
* Data Analyst
* AI/ML Engineer
* Web Developer

The module displays:

* Required skills
* Matching skills
* Missing skills
* Overall skill-match percentage

### 🎤 AI Interview Room

The interview module provides an interactive environment for interview practice.

Currently supported:

* Technical Interview
* HR Interview
* Python Interview
* Java Interview

The application provides:

* Interview questions
* Answer submission
* Technical score
* Communication score
* Relevance score
* Feedback for improving answers

A **voice-answer feature is planned for a future version**.

### 📚 Learning Roadmap

The Learning Roadmap provides a step-by-step learning path based on the selected career goal.

Available roadmaps include:

* Python Developer
* Java Developer
* Data Analyst
* AI/ML Engineer

---

## 🛠️ Technologies Used

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Application development      |
| Streamlit     | Web application and UI       |
| HTML/CSS      | UI customization             |
| Pandas        | Data processing              |
| NumPy         | Numerical operations         |
| Scikit-learn  | Machine learning integration |
| NLP Libraries | Future resume/skill analysis |
| Google Gemini | Planned AI integration       |

---

## 📁 Project Structure

```text
career_copilot/
│
├── app.py
├── README.md
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/career-copilot.git
```

### 2. Open the project

```bash
cd career-copilot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🖥️ Application Workflow

```text
                 ┌───────────────────┐
                 │   Career Copilot  │
                 └─────────┬─────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
       Resume Analysis              Career Selection
             │                           │
             ▼                           ▼
       Resume Score                 Skill Gap
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
                    Interview Practice
                           │
                           ▼
                    Learning Roadmap
```

---

## 🎯 Target Users

Career Copilot is mainly designed for:

* College students
* Freshers
* Students preparing for placements
* Students preparing for technical interviews
* Students looking for a structured career roadmap

---

## 🔮 Future Enhancements

The project can be extended with several AI-powered features:

* 🤖 AI-based resume analysis
* 📑 Automatic PDF/DOCX resume text extraction
* 🧠 NLP-based skill extraction
* 🎯 AI-powered career recommendations
* 🎤 Voice-based interview interaction
* 🗣️ Speech-to-text interview answers
* 🤖 AI-generated interview questions
* 📊 Detailed interview performance reports
* 💬 AI career chatbot
* 📚 Personalized learning recommendations
* 📄 Automated career-readiness report
* 🔗 Job-role and skill recommendations

---

## 📌 Current Status

**Project Status: 🚧 In Development**

The current version includes the main Career Copilot interface and working modules for:

* Dashboard
* Resume Analyzer interface
* Skill Gap Analysis
* Interview Practice
* Learning Roadmap

AI-powered analysis and voice interaction are planned for future updates.

---

## 👩‍💻 Developer

**Aduri Manisha**

B.Tech – Computer Science and Engineering
Malla Reddy Engineering College for Women

---

## ⭐ Acknowledgement

This project was developed as an academic project to explore **Python, Streamlit, career guidance systems, resume analysis, and AI-assisted interview preparation**.

---

## 📜 License

This project is intended for educational and academic purposes.
