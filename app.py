import streamlit as st
from ai_module import get_response
with st.sidebar:
    system_prompt = st.text_area(
        "System Prompt", """You are a career assistant helping a student decide on a career path. The student will describe their interests, and you will provide a career recommendation based on their interests.""")
st.title("💬 Quess app test")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "What are your interests. I will help you find a career path based on your interests. Please describe your interests in a few sentences. \n eg. I like making stuff and im also pretty good at maths."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = get_response(system_prompt, prompt)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
