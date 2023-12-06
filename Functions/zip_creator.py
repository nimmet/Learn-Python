import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_dir,"w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ =="__main__":
    make_archive(["day17Bonus.py","gui.py"],"Functions")