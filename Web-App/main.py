import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Web-App/images/uyghur.png")


with col2:
    st.title("Uyghur Man")
    content = """
    Hei, I am Uyghur. I am a python learner and I want to be a python programmer soon. Hallo, Mein name ist Uyghur. Ich bin
     ein Python Lerneren. Ich mochte ein Python Programmierer werden.
    """
    st.info(content)