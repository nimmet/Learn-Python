import PySimpleGUI as sg


name_label = sg.Text("Name: ")
name_input = sg.InputText(tooltip="Enter your name")

pass_label = sg.Text("Password: ")
pass_input = sg.InputText(tooltip="Enter your password",password_char="*")
login = sg.Button("Login")

window = sg.Window("Login Screen", layout=[[name_label, name_input],
                                           [pass_label, pass_input],
                                           [login]])

window.read()
window.close()