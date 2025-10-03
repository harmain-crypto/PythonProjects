# Write a Python script that takes a list of words as input and creates
# a new list containing only the words with three or more characters using
# list slicing. Print the new list.

words = []
while(True):
    word = input("Enter a word or press 0 to exit the loop :")
    if word == "0":
        break

    words.append(word)
sliceWOrds = []
for word in words:
    if word[2:]:
        sliceWOrds.append(word)

print(sliceWOrds)