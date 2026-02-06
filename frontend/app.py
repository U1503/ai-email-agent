import streamlit as st
import requests

st.title("📧 AI Email Agent")

if "generated_data" not in st.session_state:
    st.session_state.generated_data = None

if st.button("Generate Reply"):
    response = requests.get("http://127.0.0.1:8000/run-agent")

    if response.status_code == 200:
        st.session_state.generated_data = response.json()
    else:
        st.error("Backend not running!")

# Show generated content
if st.session_state.generated_data:
    data = st.session_state.generated_data

    st.success("Reply Generated!")

    st.subheader("📌 Category")
    st.write(data.get("category"))

    st.subheader("✉️ Generated Reply")
    st.text_area("Edit Reply Before Sending:",
                 value=data.get("reply"),
                 height=250,
                 key="editable_reply")

    if st.button("✅ Approve & Send"):
        send_response = requests.post(
            "http://127.0.0.1:8000/send-email",
            json={
                "subject": data.get("subject"),
                "reply": st.session_state.editable_reply
            }
        )

        if send_response.status_code == 200:
            st.success("Email Sent Successfully!")
        else:
            st.error("Sending Failed")
