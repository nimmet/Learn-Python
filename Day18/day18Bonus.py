import PySimpleGUI as sg
from Functions.zip_extractor import *

sg.theme("LightBrown")

archive_text = sg.Text("Select archive:  ")
dest_text = sg.Text("Select dest dir: ")

archive_input = sg.Input()
dest_input = sg.Input()

archive_button = sg.FileBrowse("Choose", key="archive")
dest_button = sg.FolderBrowse("Choose", key="dest")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Extract File from Archive", layout=[
    [archive_text, archive_input, archive_button],
    [dest_text,dest_input, dest_button],
    [extract_button, output_label]
])

while True:
    event, values = window.read()
    extract_archive(values["archive"], values["dest"])
    window["output"].update(value="Extraction completed!", font=("Helvetica",20))

window.close()