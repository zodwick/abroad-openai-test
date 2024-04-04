import streamlit as st
from ai_module import web_search
with st.sidebar:
    schoolname = st.text_input(
        "School Name", key="schoolname")
    school_website = st.text_input(
        "School Website ", key="school_website", )
    language = st.text_input(
        "Preffered language ", key="language", )
st.title("💬 Veranda School Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not school_website or not schoolname:
        st.info("Please provide the school name and website.")
        st.stop()

    if not language:
        language = "english"

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg, urls = web_search(prompt, school_website, schoolname, language)
    if urls:
        st.sidebar.divider()
        st.sidebar.markdown("Referred Links")
        for url in urls:
            st.sidebar.markdown(f"- [{url}]({url})")
        st.sidebar.divider()
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
