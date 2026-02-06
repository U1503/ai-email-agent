import streamlit as st
import requests

st.title("📧 AI Email Agent")

if st.button("Generate Reply"):
    response = requests.get("http://127.0.0.1:8000/run-agent")
    if response.status_code == 200:
        data = response.json()
    else:
        st.error(f"Backend error: {response.text}")
        st.stop()

    st.success("Reply Generated!")

    st.subheader("Category")
    st.write(data["category"])

    st.subheader("Generated Reply")
    st.text_area("Edit before sending", data["reply"], height=300)

    if st.button("Approve & Send"):
        send = requests.post(
            "http://127.0.0.1:8000/send-email",
            json=data
        )
        st.success(send.json()["status"])
