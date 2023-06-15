import os, re

pattern = r'\d{3}-\d{3}-\d{4}'
path = os.getcwd() + "\\Root"
print(path)

for folder, sub_folder, file in os.walk(path):
    for sub_fold in sub_folder:
        pass
    for f in file:
        if f.endswith('.txt'):
            with open(folder + "\\" + f, 'r') as textfile:
                text_content = textfile.read()
                match = re.search(pattern, text_content)
                if match is not None:
                    print(match.group())
