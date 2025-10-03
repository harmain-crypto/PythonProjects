import re
def unique_words(file_path):
    with open(file_path,"r") as file:
        content = file.read()
        content = content.lower()
    s = re.findall(r"\b\w+\b", content)
    
    print(s)
unique_words("sample.txt")