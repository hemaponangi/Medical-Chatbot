import streamlit as st
from openai import OpenAI

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ------------------ DISCLAIMER ------------------
DISCLAIMER = (
    "⚠️ **Disclaimer:** This chatbot provides general health information "
    "and is not a substitute for professional medical advice. "
    "Please consult a qualified healthcare professional."
)

# ------------------ OPENAI CLIENT ------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ------------------ SESSION STATE ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ UI ------------------
st.title("🩺 AI Health FAQ Chatbot")
st.markdown(DISCLAIMER)
st.divider()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Ask a health-related question...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a health FAQ assistant. "
                            "Provide general, safe health information. "
                            "Avoid diagnosis and prescriptions."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )

            answer = response.choices[0].message.content
            final_answer = f"{answer}\n\n{DISCLAIMER}"

            st.markdown(final_answer)

            # Save assistant response
            st.session_state.messages.append(
                {"role": "assistant", "content": final_answer}
            )
