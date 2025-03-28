
import streamlit as st
import random

# APC MC 題庫
questions = [
    {
        "question": "What is the primary purpose of the RICS Global Professional and Ethical Standards?",
        "options": ["To regulate property prices", "To ensure professional integrity", "To increase RICS membership", "To enforce contract laws"],
        "answer": "To ensure professional integrity"
    },
    {
        "question": "Which contract type is most commonly used in construction projects with a fixed price?",
        "options": ["Cost-plus contract", "Lump sum contract", "Time and materials contract", "Framework agreement"],
        "answer": "Lump sum contract"
    },
    {
        "question": "In MEP cost estimation, what does 'value engineering' primarily aim to achieve?",
        "options": ["Reduce costs without compromising quality", "Increase overall project cost", "Eliminate all MEP systems", "Extend project duration"],
        "answer": "Reduce costs without compromising quality"
    },
    {
        "question": "Under the RICS rules, what is the key responsibility of a Quantity Surveyor?",
        "options": ["Provide cost control and financial advice", "Design structural elements", "Manage on-site construction workers", "Provide legal representation"],
        "answer": "Provide cost control and financial advice"
    }
]

# 初始化 Streamlit App
st.title("📘 APC MC Practice (Cloud Version)")

# 隨機抽取題目
question = random.choice(questions)
st.subheader(question["question"])

# 用戶選擇答案
selected_option = st.radio("Choose the correct answer:", question["options"])

# 顯示結果
if st.button("Submit"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: {question['answer']}")

st.info("Practice APC multiple-choice questions to prepare for your exam.")
