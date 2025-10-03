# Write a Python script that takes a list of numbers
# as input and uses a lambda function with map() to calculate
# the square of each number and print the results.

numbers = []
while(True):
    num = input("Enter a number or write \"exit\" to exit the loop :")
    if num.lower()=="exit":
        break
    num = int(num)
    numbers.append(num)

print(f"List before lambda operation : {numbers}")
squares = list(map(lambda x: x * x, numbers))

print(f"\nList after lambda operation : {squares}")


