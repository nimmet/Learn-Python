import streamlit as st
from functions import *

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("You can make any web app here")

todos = get_todos()

for todo in todos:
    st.checkbox(todo,key=todo)

st.text_input(label="Enter a todo: ", placeholder="Add a todo")