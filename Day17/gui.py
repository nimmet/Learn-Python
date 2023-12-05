from Functions.functions import *
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
todo_List = sg.Listbox(values=[],key="todo_list", )


window = sg.Window("To-do App", layout=[[label],[input_box,add_button],
                                        [todo_List]], font=("Helvetica",20))
while True:
    event,values = window.read()

    match event:
        case "Add":
            todos = get_todos()
            todos.append(values["todo"].title()+"\n")
            write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()