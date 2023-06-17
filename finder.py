import os, re
import unzipfile

pattern = r'\d{3}-\d{3}-\d{4}'
path = os.getcwd() + "\\Root"
print(path)

for folder, sub_folder, file in os.walk(path):  # Loop to unzip any zip files
    for f in file:
        if f.endswith('.zip'):
            unzipfile.unzipping(folder, f)

for folder, sub_folder, file in os.walk(path):  # Loop to read all the data in the .txt files
    for f in file:
        if f.endswith('.txt'):
            with open(folder + "\\" + f, 'r') as textfile:
                text_content = textfile.read()
                match = re.search(pattern, text_content)
                if match is not None:
                    print(match.group())

