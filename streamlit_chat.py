import streamlit as st
import requests
import fitz
import time

st.set_page_config(page_title="STAN Chatbot", page_icon="💬")

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
                const submitBtn = window.parent.document.querySelector('button[type="submit"]');
                if (submitBtn) submitBtn.click();
            }
        });
    }
    </script>
""", unsafe_allow_html=True)

# Form with text_area (Enter to submit, Shift+Enter for newline)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("Your message:", height=40)
    submitted = st.form_submit_button("Send")

# Chat logic
if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = None
    try:
        response = requests.post("https://stan-chatbot-backend.onrender.com", json={
            "user_id": st.session_state.user_id,
            "message": user_input
        })
        if response.status_code == 200:
            reply = response.json().get("response", "🤖: Sorry, I couldn’t understand that.")
        else:
            reply = f"⚠️ Server error: {response.status_code}"
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    # Simulate typing animation only if reply is safe
    if reply:
        streamed_reply = ""
        placeholder = st.empty()
        for word in reply.split():
            streamed_reply += word + " "
            placeholder.markdown(f"🤖: {streamed_reply}")
            time.sleep(0.04)
        st.session_state.messages.append({"role": "assistant", "content": streamed_reply})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(f"{'👤' if msg['role'] == 'user' else '🤖'}: {msg['content']}")

# Optional PDF upload
uploaded_pdf = st.file_uploader("📄 Upload a PDF", type="pdf")
if uploaded_pdf:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    summary_prompt = f"Summarize this document:\n{text[:2000]}"
    st.session_state.messages.append({"role": "user", "content": summary_prompt})

    try:
        response = requests.post("https://stan-chatbot-backend.onrender.com", json={
            "user_id": st.session_state.user_id,
            "message": summary_prompt
        })
        summary_reply = response.json().get("response", "⚠️ Summary failed.")
    except Exception as e:
        summary_reply = f"⚠️ Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": summary_reply})
