import os
import streamlit as st
from ai_module import get_response
import hmac
from dotenv import load_dotenv
load_dotenv()


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], os.getenv("password")):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.


with st.sidebar:
    system_prompt = st.text_area(
        "System Prompt", """You are a career assistant helping a student decide on a career path. The student will describe their interests, and you will provide a career recommendation based on their interests. Do not reply to any messages that are not related to career recommendations.""", height=250)
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
