
import streamlit as st



st.header("Contact Me")

with st.form(key="email_forms"):

    user_email = st.text_input("You email address")
    message = st.text_area("You Message")
    button = st.form_submit_button("Submit")

    if button:
        st.info("I was pressed!")