import PySimpleGUI as sg

from_Button = sg.FileBrowse("Choose")
to_Button = sg.FolderBrowse("Choose")
compress_Button = sg.Button("Compress")

from_Label = sg.Text("Select files to compress")
to_Label = sg.Text("Select destination folder")

from_Input = sg.Input()
to_Input = sg.Input()

window = sg.Window("File Zipper", layout=[[from_Label,from_Input,from_Button],
                                          [to_Label,to_Input,to_Button],[compress_Button]])
window.read()

window.close()