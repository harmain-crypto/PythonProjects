



def Input(n):
    for x in range(0,n):
        words = []
        word = input("Enter a Word:")
        words.append(word)
    return words

def dictonary(words=[]):
    length = []
    if len(words)==0:
        print("No Words Added")
    for word in words:
        length.append(len(word))
    len_dict = {}  
    for i in range(len(words)):
        len_dict[words[i]] = length[i]
    return len_dict

def description():
    print("This Program is used to create a dictionary where the keys are the words, and the values are the lengths of the corresponding words")
