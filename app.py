import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

# ---------------- CUSTOM CSS (DARK THEME) ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: Arial, sans-serif;
        color: #e0e0e0;
    }

    .card {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.8);
        margin-top: 40px;
    }

    h1 {
        text-align: center;
        color: #80cbc4;
    }

    .stTextInput > div > div > input {
        background-color: #2c2c2c;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #555;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: #b0bec5;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- UI ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.title("🩺 AI Health FAQ Chatbot")
st.write("Ask simple health-related questions")

faq = {
    "fever": "Fever is a temporary increase in body temperature. Drink fluids and rest. See a doctor if it lasts more than 2 days.",
    "cold": "Common cold causes runny nose and sneezing. Rest and warm fluids help.",
    "headache": "Headache can be due to stress or dehydration. Drink water and rest.",
    "cough": "Cough may be due to cold or allergy. Warm water and honey may help.",
    "covid": "COVID-19 symptoms include fever, cough, and breathing issues. Get tested if symptoms appear.",
    "diabetes": "Diabetes is a condition where blood sugar levels are high. Regular checkups are important.",
    "bp": "High blood pressure can cause heart problems. Reduce salt and stress."
}

user_input = st.text_input("Enter your health question:")

if user_input:
    found = False
    for key in faq:
        if key in user_input.lower():
            st.success(faq[key])
            found = True
            break

    if not found:
        st.warning("Sorry, I can answer only basic health FAQs. Please consult a doctor.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>⚠️ This chatbot provides basic information only. Not a medical diagnosis.</div>",
    unsafe_allow_html=True
)
