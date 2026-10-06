import streamlit as st

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Career Copilot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# CUSTOM CSS
# -----------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

.card {
    padding: 22px;
    border-radius: 18px;
    background-color: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.score {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

.small-text {
    color: #6b7280;
    font-size: 14px;
}

.feature-title {
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# SIDEBAR
# -----------------------------------------

st.sidebar.title("🎯 Career Copilot")

st.sidebar.caption("AI-powered career assistant")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "🧠 Skill Gap",
        "🎤 AI Interview",
        "📚 Learning Roadmap"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("👤 Student Profile")

name = st.sidebar.text_input(
    "Name",
    placeholder="Enter your name"
)

education = st.sidebar.text_input(
    "Education",
    placeholder="B.Tech CSE"
)

skills = st.sidebar.text_input(
    "Skills",
    placeholder="Python, Java, SQL"
)

target_role = st.sidebar.selectbox(
    "Target Role",
    [
        "Software Developer",
        "Python Developer",
        "Data Analyst",
        "AI/ML Engineer",
        "Web Developer"
    ]
)


# -----------------------------------------
# DASHBOARD
# -----------------------------------------

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">

    <h1>🎯 Career Copilot</h1>

    <p>
    Your personal AI-powered career guidance assistant
    </p>

    </div>
    """, unsafe_allow_html=True)

    if name:
        st.subheader(f"👋 Welcome, {name}!")

    else:
        st.subheader("👋 Welcome!")

    st.write(
        "Build your career profile, analyze your resume, "
        "identify skill gaps and practice interviews."
    )

    st.divider()

    # -----------------------------------------
    # CAREER READINESS
    # -----------------------------------------

    st.subheader("📊 Career Readiness")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Resume Score",
            "82 / 100",
            "+8"
        )

    with col2:
        st.metric(
            "Skill Match",
            "76%",
            "+12%"
        )

    with col3:
        st.metric(
            "Interview Score",
            "8.4 / 10",
            "+0.8"
        )

    with col4:
        st.metric(
            "Career Readiness",
            "81%",
            "+10%"
        )

    st.divider()

    # -----------------------------------------
    # FEATURES
    # -----------------------------------------

    st.subheader("🚀 Career Tools")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <div class="feature-title">
        📄 Resume Analyzer
        </div>

        <p>
        Upload your resume and get an AI-powered
        resume score, skill analysis and improvement
        suggestions.
        </p>

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Analyze My Resume",
            use_container_width=True
        ):
            st.info(
                "Go to Resume Analyzer from the sidebar."
            )

    with col2:

        st.markdown("""
        <div class="card">

        <div class="feature-title">
        🎤 AI Interview
        </div>

        <p>
        Practice interviews with AI, answer questions
        using text or voice and receive instant feedback.
        </p>

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Start AI Interview",
            use_container_width=True
        ):
            st.info(
                "Go to AI Interview from the sidebar."
            )


# -----------------------------------------
# RESUME ANALYZER
# -----------------------------------------

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")

    st.write(
        "Upload your resume to analyze its overall strength."
    )

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "txt", "docx"]
    )

    if uploaded_file:

        st.success(
            f"Resume uploaded: {uploaded_file.name}"
        )

        st.divider()

        if st.button(
            "🔍 Analyze Resume",
            use_container_width=True
        ):

            st.subheader("📊 Resume Analysis")

            # Demo score for now
            resume_score = 82

            col1, col2 = st.columns([1, 2])

            with col1:

                st.markdown(
                    f"""
                    <div class="card">

                    <div class="small-text">
                    RESUME SCORE
                    </div>

                    <div class="score">
                    {resume_score}/100
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                st.write("### Resume Strength")

                st.progress(
                    resume_score / 100
                )

                st.write(
                    "Your resume has a good overall structure."
                )

            st.divider()

            # -----------------------------------------
            # ANALYSIS DETAILS
            # -----------------------------------------

            st.subheader("🔎 Analysis Details")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Skills",
                    "88%"
                )

            with col2:

                st.metric(
                    "Projects",
                    "80%"
                )

            with col3:

                st.metric(
                    "ATS Compatibility",
                    "79%"
                )

            st.divider()

            st.subheader("✅ Strengths")

            st.success(
                "Technical skills are clearly mentioned."
            )

            st.success(
                "Education information is present."
            )

            st.success(
                "Projects and certifications improve your profile."
            )

            st.subheader("⚠️ Suggestions")

            st.warning(
                "Add measurable achievements to your projects."
            )

            st.warning(
                "Use stronger action verbs in your experience section."
            )

            st.warning(
                "Add more keywords related to your target role."
            )

    else:

        st.info(
            "Upload your resume to begin the analysis."
        )


# -----------------------------------------
# SKILL GAP
# -----------------------------------------

elif page == "🧠 Skill Gap":

    st.title("🧠 Skill Gap Analyzer")

    st.write(
        "Compare your current skills with the skills "
        "required for your target career."
    )

    st.divider()

    st.subheader(
        f"Target Career: {target_role}"
    )

    if skills:

        user_skills = [
            skill.strip().lower()
            for skill in skills.split(",")
            if skill.strip()
        ]

        required_skills = {
            "Software Developer": [
                "python",
                "java",
                "sql",
                "git",
                "data structures"
            ],

            "Python Developer": [
                "python",
                "sql",
                "git",
                "flask",
                "api"
            ],

            "Data Analyst": [
                "python",
                "sql",
                "excel",
                "statistics",
                "power bi"
            ],

            "AI/ML Engineer": [
                "python",
                "numpy",
                "pandas",
                "machine learning",
                "deep learning"
            ],

            "Web Developer": [
                "html",
                "css",
                "javascript",
                "git",
                "react"
            ]
        }

        required = required_skills[target_role]

        matched = [
            skill
            for skill in required
            if skill in user_skills
        ]

        missing = [
            skill
            for skill in required
            if skill not in user_skills
        ]

        match_percentage = int(
            (len(matched) / len(required)) * 100
        )

        st.subheader("📊 Skill Match")

        st.progress(
            match_percentage / 100
        )

        st.write(
            f"**{match_percentage}%** match for {target_role}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Skills You Have")

            if matched:

                for skill in matched:
                    st.success(skill.title())

            else:

                st.info("No matching skills found.")

        with col2:

            st.subheader("❌ Skills to Learn")

            if missing:

                for skill in missing:
                    st.warning(skill.title())

            else:

                st.success(
                    "You have all the required skills!"
                )

    else:

        st.warning(
            "Enter your skills in the sidebar first."
        )


# -----------------------------------------
# AI INTERVIEW
# -----------------------------------------

elif page == "🎤 AI Interview":

    st.title("🎤 AI Interview Room")

    st.write(
        "Practice your interview with an AI career coach."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"🎯 Target Role: {target_role}"
        )

    with col2:

        st.info(
            "📝 Question: 1 / 10"
        )

    st.divider()

    st.subheader("🤖 Interviewer")

    st.markdown(
        """
        ### Tell me about yourself.

        Explain your education, technical skills,
        projects and career interests.
        """
    )

    st.divider()

    st.subheader("🎙️ Answer")

    answer_method = st.radio(
        "Choose how you want to answer",
        [
            "⌨️ Type Answer",
            "🎙️ Voice Answer"
        ]
    )

    if answer_method == "⌨️ Type Answer":

        answer = st.text_area(
            "Your Answer",
            placeholder="Type your answer here...",
            height=180
        )

        if st.button(
            "Submit Answer",
            use_container_width=True
        ):

            if answer:

                st.success(
                    "Answer submitted successfully!"
                )

                st.subheader("🤖 AI Feedback")

                st.metric(
                    "Answer Score",
                    "82 / 100"
                )

                st.write(
                    "### 💡 Feedback"
                )

                st.write(
                    "Your answer is clear and relevant. "
                    "Try adding one specific project example "
                    "to make your answer stronger."
                )

            else:

                st.warning(
                    "Please enter your answer first."
                )

    else:

        st.info(
            "🎙️ Voice interview mode will be connected "
            "to speech recognition in the next stage."
        )

        if st.button(
            "🎙️ Start Voice Interview",
            use_container_width=True
        ):

            st.info(
                "Voice interview module is ready to be integrated."
            )


# -----------------------------------------
# LEARNING ROADMAP
# -----------------------------------------

elif page == "📚 Learning Roadmap":

    st.title("📚 Personalized Learning Roadmap")

    st.write(
        f"Recommended learning path for **{target_role}**"
    )

    st.divider()

    roadmap = {
        "Python Developer": [
            "Python Fundamentals",
            "Object-Oriented Programming",
            "SQL & Databases",
            "REST APIs",
            "Flask / FastAPI",
            "Git & GitHub",
            "Build Real Projects"
        ],

        "Data Analyst": [
            "Python",
            "Pandas & NumPy",
            "SQL",
            "Statistics",
            "Data Visualization",
            "Power BI",
            "Real-world Projects"
        ],

        "AI/ML Engineer": [
            "Python",
            "NumPy & Pandas",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Generative AI"
        ],

        "Software Developer": [
            "Programming Fundamentals",
            "Data Structures",
            "Algorithms",
            "OOP",
            "SQL",
            "Git & GitHub",
            "Projects"
        ],

        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "Responsive Design",
            "Git & GitHub",
            "React",
            "Web Projects"
        ]
    }

    steps = roadmap[target_role]

    for i, step in enumerate(steps, start=1):

        st.write(
            f"### {i}. {step}"
        )

        st.progress(
            min(i / len(steps), 1.0)
        )

    st.success(
        "Complete these skills step-by-step to improve "
        "your career readiness."
    )