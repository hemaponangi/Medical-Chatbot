import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ---------------- CUSTOM CSS (DARK MEDICAL THEME) ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: Arial, sans-serif;
        color: #e0e0e0;
    }

    h1 {
        text-align: center;
        color: #80cbc4;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: #b0bec5;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- FAQ DATA ----------------
faq = {
    ("fever", "temperature"): "Fever is a temporary increase in body temperature. Drink fluids and rest. See a doctor if it lasts more than 2 days.",
    ("cold", "sneezing", "runny nose"): "Common cold causes sneezing and runny nose. Rest and warm fluids can help.",
    ("headache", "migraine"): "Headache may be caused by stress or dehydration. Drink water and take rest.",
    ("cough",): "Cough may be due to infection or allergy. Warm water and honey may help.",
    ("covid", "corona"): "COVID-19 symptoms include fever, cough, and breathing issues. Get tested if symptoms appear.",
    ("diabetes", "sugar"): "Diabetes is a condition where blood sugar levels are high. Regular monitoring is important.",
    ("bp", "blood pressure"): "High blood pressure increases heart risk. Reduce salt, stress, and exercise regularly."
}

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- UI ----------------
st.title("🩺 AI Health FAQ Chatbot")
st.write("Ask simple health-related questions")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask a health-related question...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = None
    user_text = user_input.lower()

    for keywords, answer in faq.items():
        if any(word in user_text for word in keywords):
            response = answer
            break

    if not response:
        response = (
            "Sorry, I can answer only basic health FAQs.\n\n"
            "⚠️ Please consult a doctor for accurate medical advice."
        )

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>⚠️ This chatbot provides basic health information only. Not a medical diagnosis.</div>",
    unsafe_allow_html=True
)

