import streamlit as st
from functions import *

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("You can make any web app here")

todos = get_todos()

for todo in todos:
    st.checkbox(todo,key=todo)


st.text_input(label="Enter a todo: ", placeholder="Add a todo", on_change=add_todo, key="new_todo")

st.session_state