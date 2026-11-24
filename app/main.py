import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.chatbot import ask_chatbot, load_dataset

st.set_page_config(
    page_title="Badminton Rules Assistant",
    page_icon="🏸",
    layout="centered",
)

st.title("🏸 BWF Badminton Rules Assistant")
st.markdown("Ask me anything about badminton court dimensions, scoring systems, serving rules, faults, lets, and match regulations!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me any question about official BWF Badminton rules.",
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Type your badminton rules question here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Checking BWF rulebook..."):
            try:
                reply, context = ask_chatbot(user_input)
            except Exception as e:
                reply = f"Error: {e}"
                context = ""
        st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply, "context": context}
    )
