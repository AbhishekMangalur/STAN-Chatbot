import streamlit as st
import requests
import io
from pypdf import PdfReader
import time
import os

# Backend URL
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
).rstrip("/")

st.set_page_config(
    page_title="STAN Chatbot",
    page_icon="💬"
)

st.title("💬 STAN Chatbot")
st.subheader("Ask me anything. My tone adapts. I remember things too!")


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_id" not in st.session_state:
    st.session_state.user_id = "user123"


# HTML/JS to capture Enter key
st.markdown("""
    <script>
    const textarea = window.parent.document.querySelector('textarea');

    if (textarea) {
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();

                const submitBtn =
                    window.parent.document.querySelector(
                        'button[type="submit"]'
                    );

                if (submitBtn) {
                    submitBtn.click();
                }
            }
        });
    }
    </script>
""", unsafe_allow_html=True)


# Form with text_area
# Enter = submit
# Shift + Enter = newline
with st.form(
    key="chat_form",
    clear_on_submit=True
):
    user_input = st.text_area(
        "Your message:",
        height=40
    )

    submitted = st.form_submit_button("Send")


# Sidebar controls
with st.sidebar:
    st.header("⚙️ Controls")
    st.session_state.user_id = st.text_input("User ID:", value=st.session_state.user_id)
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Optional PDF upload (placed above chat for easy access)
with st.expander("📄 Upload a PDF for Summary", expanded=False):
    uploaded_pdf = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        key="pdf_uploader"
    )

    if uploaded_pdf and st.session_state.get("last_uploaded_pdf") != uploaded_pdf.name:
        st.session_state.last_uploaded_pdf = uploaded_pdf.name
        reader = PdfReader(io.BytesIO(uploaded_pdf.read()))
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        summary_prompt = f"Summarize this document:\n{text[:2000]}"
        st.session_state.messages.append({
            "role": "user",
            "content": summary_prompt
        })

        try:
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "user_id": st.session_state.user_id,
                    "message": summary_prompt
                },
                timeout=120
            )
            if response.status_code == 200:
                summary_reply = response.json().get(
                    "response",
                    "⚠️ Summary failed."
                )
            else:
                summary_reply = f"⚠️ Server error: {response.status_code}"
        except Exception as e:
            summary_reply = f"⚠️ Error: {e}"

        st.session_state.messages.append({
            "role": "assistant",
            "content": summary_reply
        })
        st.rerun()

# Chat logic
if submitted and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    reply = None
    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={
                "user_id": st.session_state.user_id,
                "message": user_input
            },
            timeout=120
        )

        if response.status_code == 200:
            reply = response.json().get(
                "response",
                "🤖: Sorry, I couldn't understand that."
            )
        else:
            reply = f"⚠️ Server error: {response.status_code}"

    except Exception as e:
        reply = f"⚠️ Error: {e}"

    if reply:
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
    st.rerun()

# Display chat history in reverse order (newest messages at the top, older ones below)
turns = []
current_turn = []
for msg in st.session_state.messages:
    if msg.get("role") == "user" and current_turn:
        turns.append(current_turn)
        current_turn = [msg]
    else:
        current_turn.append(msg)
if current_turn:
    turns.append(current_turn)

for turn in reversed(turns):
    for msg in turn:
        with st.chat_message(
            "user" if msg["role"] == "user" else "assistant"
        ):
            st.markdown(
                f"{'👤' if msg['role'] == 'user' else '🤖'}: "
                f"{msg['content']}"
            )
