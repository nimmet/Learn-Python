import pandas
import streamlit as st
import pandas as pd

df = pandas.read_csv("Student-Project/topics.csv")


with st.form(key="email_form"):
    email = st.text_input("You Email Address")
    topic = st.selectbox("What topic do you want to discuss?",df["topic"])
    text_message = st.text_area("Text")
    button = st.form_submit_button("Submit")

    message = f"""\
    Subject: New email from {email}
    
    From: {email}
    Topic {topic}
    {text_message}
    """

    if button:
        pass
        st.info("Your email was sent successfully")

