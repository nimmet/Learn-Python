import streamlit as st
import pandas as pd

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

# st.subheader("I have some plans about my future career")
# st.image("Web-App/images/1.png")

content1 = """
Below you find out some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content1)


col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("Web-App/data.csv", sep=";")

with col3:
  for index, row in df[:10].iterrows():
      st.header(row["title"])
      st.write(row["description"])
      st.image("Web-App/images/"+row["image"])
      st.write("[Source Code](https://www.bing.com)")

with empty_col:
    pass

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Web-App/images/" + row["image"])
        st.write("[Source Code](https://www.bing.com)")