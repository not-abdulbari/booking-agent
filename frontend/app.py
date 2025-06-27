import streamlit as st
import requests

st.title("📅 AI Google Calendar Booking Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role, content = message
    with st.chat_message(role):
        st.markdown(content)

prompt = st.chat_input("Ask to book an appointment...")

if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            res = requests.post("http://localhost:8000/chat", json={"input": prompt})
            if res.status_code == 200:
                reply = res.json().get("response", "❌ No response key in result.")
            else:
                reply = f"❌ Backend error {res.status_code}: {res.text}"

        except Exception as e:
            reply = f"❌ Error: {e}"
        st.markdown(reply)
    st.session_state.messages.append(("assistant", reply))