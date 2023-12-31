import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


st.subheader("Our Team")

col1,sp1, col2, sp2, col3 = st.columns([1.5,0.2,1.5,0.2,1.5])

df = pd.read_csv("Student-Project/data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first'].capitalize()} {row['last'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image("Student-Project/images/"+row["image"])

with sp1:
    pass

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first'].capitalize()} {row['last'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image("Student-Project/images/"+row["image"])

with sp2:
    pass

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first'].capitalize()} {row['last'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image("Student-Project/images/"+row["image"])




