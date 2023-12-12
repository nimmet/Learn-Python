from Functions.functions import *
import PySimpleGUI as sg
import time

sg.theme("LightBrown")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),key="todos", enable_events=True, size=[45,10] )
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("To-do App", layout=[[clock],[label],[input_box,add_button],
                                        [list_box, edit_button, complete_button],
                                        [exit_button]], font=("Helvetica",20))
while True:
    event,values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            todos.append(values["todo"].title()+"\n")
            write_todos(todos)
            window["todos"].update(values=todos)


        case "Edit":
            try:
                window["todo"].update(value=values["todos"][0])
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.title()+"\n"
                write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))

        case "Complete":
            try:
                window["todo"].update(value=values["todos"][0])
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))





        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()