import streamlit as st

with st.chat_message("user"):
    st.write("Hello, how are you?")
prompt = st.chat_input("궁금한게있으면 물어봐봐")