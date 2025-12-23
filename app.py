import streamlit as st
import time
from openai import OpenAI

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ------------------ DISCLAIMER ------------------
DISCLAIMER = (
    "⚠️ **Disclaimer:** This chatbot provides general health information only "
    "and is not a substitute for professional medical advice. "
    "Please consult a qualified healthcare professional."
)

# ------------------ UI HEADER ------------------
st.title("🩺 AI Health FAQ Chatbot")
st.markdown(DISCLAIMER)
st.divider()

# ------------------ API KEY CHECK ------------------
if "OPENAI_API_KEY" not in st.secrets:
    st.error("🚨 OpenAI API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ------------------ SESSION STATE ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_call_time" not in st.session_state:
    st.session_state.last_call_time = 0

# ------------------ DISPLAY CHAT HISTORY ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Ask a health-related question...")

if user_input:
    # ---- SIMPLE RATE LIMIT (PREVENT SPAM) ----
    if time.time() - st.session_state.last_call_time < 6:
        st.warning("⏳ Please wait a few seconds before asking another question.")
        st.stop()

    st.session_state.last_call_time = time.time()

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {
                        "role": "system",
                        "content": (
                            "You are a health FAQ assistant. "
                            "Provide only general, educational health information. "
                            "Do NOT diagnose diseases or prescribe medicines. "
                            "If symptoms sound serious, advise consulting a doctor."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            answer = response.output_text
            final_answer = f"{answer}\n\n{DISCLAIMER}"

            st.markdown(final_answer)

            # Save assistant message
            st.session_state.messages.append(
                {"role": "assistant", "content": final_answer}
            )
