import PySimpleGUI as sg
from Functions.zip_creator import *

from_Button = sg.FilesBrowse("Choose",key="files")
to_Button = sg.FolderBrowse("Choose", key="folder")
compress_Button = sg.Button("Compress")

from_Label = sg.Text("Select files to compress")
to_Label = sg.Text("Select destination folder")

from_Input = sg.Input()
to_Input = sg.Input()
output_label = sg.Text(key="output", text_color="green")

while True:
    window = sg.Window("File Zipper", layout=[[from_Label,from_Input,from_Button],
                                          [to_Label,to_Input,to_Button],[compress_Button,output_label]])
    event,values = window.read()
    filepaths = values["files"].split(";")
    dest_dir = values["folder"]
    make_archive(filepaths,dest_dir)
    window["output"].update(value="Compressesion Completed")


window.close()