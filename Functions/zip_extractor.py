import zipfile

def extract_archive(archivePath, dest_dir):
    with zipfile.ZipFile(archivePath,'r') as archive:
        archive.extractall(dest_dir)