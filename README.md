# FileAutomation
File Automation tasks using Python, which includes reading through all the folders and files in the root folder with the end goal of finding a given value in one of the text files using Regex.

## Code Explanation
The aim here is to find a phone number in the format ###-###-####.
However, this code can be repurposed to search for any value or even a list of values with slight modification.

Setting up the Regex Pattern
```commandline
pattern = r'\d{3}-\d{3}-\d{4}'
```
Traversing through all the folders/sub folders and reading all the **.txt** files in the given root folder
```commandline
for folder, sub_folder, file in os.walk(path):
    for sub_fold in sub_folder:
        pass
    for f in file:
        if f.endswith('.txt'):
            with open(folder + "\\" + f, 'r') as textfile:
                text_content = textfile.read()
```

Check for a match using the search method from re module and print out the result
```commandline
                match = re.search(pattern, text_content)
                if match is not None:
                    print(match.group())
```