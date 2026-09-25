import streamlit as st
import pandas as pd
import random

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Pak Navy Polytechnic Institute (PNPI)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM VIP CSS DESIGN
# ============================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
}
h1, h2, h3, h4 {
    color: #FFD700 !important;
    font-family: 'Georgia', serif;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}
.main-title {
    background: linear-gradient(90deg, #000428 0%, #004e92 100%);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    border: 3px solid #FFD700;
    box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
    margin-bottom: 20px;
}
.main-title h1 {
    color: #FFD700 !important;
    font-size: 42px;
    margin: 0;
}
.main-title p {
    color: #ffffff;
    font-size: 18px;
    margin-top: 8px;
}
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #FFD700;
    margin: 10px 0;
    color: white;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #000428, #004e92);
}
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
.stButton>button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #000;
    font-weight: bold;
    border-radius: 8px;
    border: none;
    padding: 10px 25px;
}
div[data-testid="stMetricValue"] {
    color: #FFD700 !important;
    font-size: 28px;
}
div[data-testid="stMetricLabel"] {
    color: #ffffff !important;
}
.stTabs [data-baseweb="tab"] {
    color: white;
    background: rgba(255,255,255,0.05);
}
img {
    border-radius: 12px;
    border: 2px solid #FFD700;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# HERO BANNER
# ============================================
st.markdown("""
<div class="main-title">
    <h1>🎓 Pak Navy Polytechnic Institute (PNPI)</h1>
    <p>📍 West Wharf Road, Karachi | Excellence in Technical Education</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Pakistan_Navy_Emblem.svg/500px-Pakistan_Navy_Emblem.svg.png",
        caption="PNPI Official Logo",
        use_container_width=True
    )

# ============================================
# SIDEBAR NAVIGATION
# ============================================
st.sidebar.markdown("## 🧭 Navigation")
menu = st.sidebar.radio(
    "Select Section:",
    [
        "🏠 Home",
        "🏫 School & Classrooms",
        "⚙️ Mechatronic Engineering",
        "📚 Library",
        "🏏 Cricket Group",
        "🍽️ College Canteen",
        "👨‍🏫 Courses & Teachers",
        "📊 Student Results Portal"
    ]
)

# ============================================
# HOME
# ============================================
if menu == "🏠 Home":
    st.header("Welcome to PNPI")

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1562774053-701939374585?w=800",
            caption="PNPI Campus",
            use_container_width=True
        )
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800",
            caption="Our Institute",
            use_container_width=True
        )

    st.markdown("""
    <div class="card">
    <h3>About PNPI</h3>
    <p>Pak Navy Polytechnic Institute (PNPI) is a premier technical institution located at
    West Wharf Road, Karachi. We offer world-class education in engineering disciplines
    with a focus on discipline, excellence, and innovation.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🏫 Classrooms", "20")
    c2.metric("🎓 Students", "40")
    c3.metric("📚 Semesters", "5")
    c4.metric("⚙️ Program", "1")

    st.subheader("📍 Location")
    st.markdown("**West Wharf Road, Karachi, Pakistan**")
    st.map(pd.DataFrame({'lat': [24.8607], 'lon': [66.9910]}), zoom=12)

# ============================================
# SCHOOL & CLASSROOMS
# ============================================
elif menu == "🏫 School & Classrooms":
    st.header("🏫 School Building & 20 Classrooms")

    st.image(
        "https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=1200",
        caption="PNPI School Building",
        use_container_width=True
    )

    st.subheader("Our Classrooms")
    st.write("PNPI has **20 well-equipped modern classrooms** for quality education.")

    classroom_imgs = [
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=600",
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=600",
        "https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=600",
        "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=600",
        "https://images.unsplash.com/photo-1588072432836-e10032774350?w=600",
        "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600",
    ]

    cols = st.columns(3)
    for i, img in enumerate(classroom_imgs):
        with cols[i % 3]:
            st.image(img, caption=f"Classroom {i+1}", use_container_width=True)

# ============================================
# MECHATRONIC ENGINEERING
# ============================================
elif menu == "⚙️ Mechatronic Engineering":
    st.header("⚙️ Mechatronic Engineering Technology")

    st.image(
        "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200",
        caption="Mechatronic Engineering Lab",
        use_container_width=True
    )

    st.markdown("""
    <div class="card">
    <h3>About the Program</h3>
    <p>Mechatronic Engineering combines Mechanical, Electronics, Computer, and Control
    engineering. This 5-semester program prepares students for modern automation industry.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 Semester-wise Subjects")

    semesters = {
        "1st Semester (8 Subjects)": [
            "Applied Mathematics-I", "Applied Physics", "Engineering Drawing",
            "Workshop Practice", "Basic Electrical Engineering", "Computer Fundamentals",
            "Communication Skills", "Islamic Studies"
        ],
        "2nd Semester (7 Subjects)": [
            "Applied Mathematics-II", "Electronic Devices & Circuits",
            "Mechanical Workshop", "Engineering Materials", "Digital Logic Design",
            "Technical Report Writing", "Pakistan Studies"
        ],
        "3rd Semester (7 Subjects)": [
            "Applied Mathematics-III", "Microprocessor & Microcontroller",
            "Sensors & Transducers", "CAD/CAM", "Fluid Mechanics",
            "Electrical Machines", "Industrial Safety"
        ],
        "4th Semester (5 Subjects)": [
            "Robotics & Automation", "PLC & SCADA Systems",
            "Control Systems", "Hydraulics & Pneumatics",
            "Project Management"
        ],
        "5th Semester (5 Subjects)": [
            "Industrial Automation", "Embedded Systems Design",
            "Mechatronic System Design", "Final Year Project",
            "Industrial Training & Internship"
        ],
    }

    for sem, subjects in semesters.items():
        with st.expander(f"📘 {sem}"):
            for i, sub in enumerate(subjects, 1):
                st.write(f"**{i}.** {sub}")

    st.subheader("🔬 Mechatronic Lab")
    st.image(
        "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=1200",
        caption="Mechatronic Engineering Laboratory",
        use_container_width=True
    )

# ============================================
# LIBRARY
# ============================================
elif menu == "📚 Library":
    st.header("📚 PNPI Central Library")

    st.image(
        "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1200",
        caption="PNPI Library - Thousands of Books",
        use_container_width=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=600",
            caption="Reading Hall",
            use_container_width=True
        )
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600",
            caption="Book Collection",
            use_container_width=True
        )

    st.markdown("""
    <div class="card">
    <h3>Library Facilities</h3>
    <ul>
        <li>📖 10,000+ Engineering & Technical Books</li>
        <li>💻 Digital Library & E-Resources</li>
        <li>📰 National & International Journals</li>
        <li>🕐 Open: 8:00 AM – 8:00 PM</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# CRICKET GROUP
# ============================================
elif menu == "🏏 Cricket Group":
    st.header("🏏 PNPI Cricket Team")

    st.image(
        "https://images.unsplash.com/photo-1531415074968-036ba1b575da?w=1200",
        caption="PNPI Cricket Team",
        use_container_width=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=600",
            caption="Match in Progress",
            use_container_width=True
        )
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1624526267942-ab0ff8a3e972?w=600",
            caption="Team Practice",
            use_container_width=True
        )

    st.markdown("""
    <div class="card">
    <h3>Team Achievements</h3>
    <ul>
        <li>🏆 Karachi Inter-Polytechnic Champions 2024</li>
        <li>🥈 Sindh Region Runners-Up 2023</li>
        <li>🏏 25+ Registered Players</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# CANTEEN
# ============================================
elif menu == "🍽️ College Canteen":
    st.header("🍽️ PNPI College Canteen")

    st.image(
        "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=1200",
        caption="College Canteen",
        use_container_width=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600",
            caption="Fresh Food Counter",
            use_container_width=True
        )
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600",
            caption="Snacks & Beverages",
            use_container_width=True
        )

    st.markdown("""
    <div class="card">
    <h3>Canteen Menu Highlights</h3>
    <ul>
        <li>🍔 Burgers, Sandwiches, Rolls</li>
        <li>🍛 Fresh Desi Lunch (Biryani, Karahi)</li>
        <li>☕ Tea, Coffee, Cold Drinks</li>
        <li>🍰 Bakery Items & Snacks</li>
        <li>⏰ Timings: 8:00 AM – 5:00 PM</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# COURSES & TEACHERS
# ============================================
elif menu == "👨‍🏫 Courses & Teachers":
    st.header("👨‍🏫 Courses & Faculty")

    teachers = {
        "1st Semester": [
            ("Applied Mathematics-I", "Prof. Ahmed Raza"),
            ("Applied Physics", "Dr. Sana Khan"),
            ("Engineering Drawing", "Engr. Bilal Hussain"),
            ("Workshop Practice", "Engr. Tariq Mehmood"),
            ("Basic Electrical Engineering", "Engr. Faisal Iqbal"),
            ("Computer Fundamentals", "Mr. Usman Ali"),
            ("Communication Skills", "Ms. Ayesha Siddiqui"),
            ("Islamic Studies", "Maulana Abdul Rehman"),
        ],
        "2nd Semester": [
            ("Applied Mathematics-II", "Prof. Ahmed Raza"),
            ("Electronic Devices & Circuits", "Dr. Kamran Shah"),
            ("Mechanical Workshop", "Engr. Tariq Mehmood"),
            ("Engineering Materials", "Dr. Sana Khan"),
            ("Digital Logic Design", "Engr. Faisal Iqbal"),
            ("Technical Report Writing", "Ms. Ayesha Siddiqui"),
            ("Pakistan Studies", "Prof. Nadeem Akhtar"),
        ],
        "3rd Semester": [
            ("Applied Mathematics-III", "Prof. Ahmed Raza"),
            ("Microprocessor & Microcontroller", "Engr. Hassan Raza"),
            ("Sensors & Transducers", "Dr. Kamran Shah"),
            ("CAD/CAM", "Engr. Bilal Hussain"),
            ("Fluid Mechanics", "Engr. Tariq Mehmood"),
            ("Electrical Machines", "Engr. Faisal Iqbal"),
            ("Industrial Safety", "Mr. Usman Ali"),
        ],
        "4th Semester": [
            ("Robotics & Automation", "Dr. Kamran Shah"),
            ("PLC & SCADA Systems", "Engr. Hassan Raza"),
            ("Control Systems", "Engr. Faisal Iqbal"),
            ("Hydraulics & Pneumatics", "Engr. Tariq Mehmood"),
            ("Project Management", "Prof. Nadeem Akhtar"),
        ],
        "5th Semester": [
            ("Industrial Automation", "Dr. Kamran Shah"),
            ("Embedded Systems Design", "Engr. Hassan Raza"),
            ("Mechatronic System Design", "Engr. Bilal Hussain"),
            ("Final Year Project", "All Faculty"),
            ("Industrial Training", "Engr. Tariq Mehmood"),
        ],
    }

    for sem, subs in teachers.items():
        st.subheader(f"📘 {sem}")
        df = pd.DataFrame(subs, columns=["Subject", "Teacher"])
        st.dataframe(df, use_container_width=True, hide_index=True)

# ============================================
# STUDENT RESULTS PORTAL
# ============================================
elif menu == "📊 Student Results Portal":
    st.header("📊 Student Results Portal")
    st.write("Apna **Name** aur **Roll Number** daal kar results dekhein.")

    students = {
        "PNPI-001": "Ali Hassan",
        "PNPI-002": "Bilal Ahmed",
        "PNPI-003": "Chaudhry Usman",
        "PNPI-004": "Danish Khan",
        "PNPI-005": "Ehsan Raza",
        "PNPI-006": "Fahad Iqbal",
        "PNPI-007": "Ghulam Abbas",
        "PNPI-008": "Hamza Sheikh",
    }

    subjects = [
        "Applied Mathematics-I", "Applied Physics", "Engineering Drawing",
        "Workshop Practice", "Basic Electrical Engineering", "Computer Fundamentals",
        "Communication Skills", "Islamic Studies"
    ]

    random.seed(42)
    results_db = {}
    for roll, name in students.items():
        marks = [random.randint(40, 95) for _ in subjects]
        results_db[roll] = {"name": name, "marks": marks}

    with st.form("login_form"):
        col1, col2 = st.columns(2)
        with col1:
            input_name = st.text_input("👤 Student Name")
        with col2:
            input_roll = st.text_input("🔢 Roll Number (e.g., PNPI-001)")

        submit = st.form_submit_button("🔍 View Result")

    if submit:
        roll = input_roll.strip().upper()
        name = input_name.strip()

        if roll not in results_db:
            st.error("❌ Roll Number nahi mila. Sahi roll number daalein (PNPI-001 se PNPI-008).")
        elif results_db[roll]["name"].lower() != name.lower():
            st.error("❌ Name aur Roll Number match nahi kar rahe.")
        else:
            data = results_db[roll]
            marks = data["marks"]

            below_60 = [subjects[i] for i, m in enumerate(marks) if m < 60]
            total = sum(marks)
            percentage = total / len(marks)

            st.success(f"✅ Welcome, {data['name']} ({roll})")

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Marks", f"{total}/{len(marks)*100}")
            m2.metric("Percentage", f"{percentage:.2f}%")
            m3.metric("Subjects < 60%", len(below_60))

            if len(below_60) >= 3:
                status = "❌ FAIL"
                m4.metric("Status", status)
                st.error("🚫 Aap 3 ya zyada subjects mein 60% se kam hain — **FAIL**.")
            elif len(below_60) in [1, 2]:
                status = "⚠️ REEXAM"
                m4.metric("Status", status)
                st.warning(f"📝 Aapko **{len(below_60)} subject(s)** mein re-exam dena hoga.")
            else:
                status = "✅ PASS"
                m4.metric("Status", status)
                st.balloons()
                st.success("🎉 Mubarak ho! Aap tamam subjects mein PASS ho gaye.")

            st.subheader("📋 Subject-wise Marks")
            df = pd.DataFrame({
                "Subject": subjects,
                "Marks": marks,
                "Percentage": [f"{m}%" for m in marks],
                "Status": ["✅ Pass" if m >= 60 else "❌ Fail" for m in marks]
            })
            st.dataframe(df, use_container_width=True, hide_index=True)

            if below_60:
                st.subheader("⚠️ Re-exam Subjects")
                for s in below_60:
                    st.write(f"- {s}")

    with st.expander("ℹ️ Demo Roll Numbers (Test ke liye)"):
        demo_df = pd.DataFrame(
            [(r, n) for r, n in students.items()],
            columns=["Roll Number", "Student Name"]
        )
        st.dataframe(demo_df, use_container_width=True, hide_index=True)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#FFD700; padding:15px;'>
    <b>🎓 Pak Navy Polytechnic Institute (PNPI)</b><br>
    West Wharf Road, Karachi | © 2025 All Rights Reserved
</div>
""", unsafe_allow_html=True)
