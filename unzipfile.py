import shutil, zipfile


# Simple code with folder and file name being passed in from the main Readdata.py file, if there are some folders to
# be unzipped

def unzipping(folder, file):
    with zipfile.ZipFile(folder + '\\' + file) as item:
        item.extractall(folder + '\\')