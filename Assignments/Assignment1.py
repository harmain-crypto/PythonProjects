# Part 1: Variable Declaration and Data Types
print("Part#1")
# Question 1: Variable Assignment
name = "Behram Saqlain"  # String variable to store name
age = 18   # Integer variable to store age
height = 1.7  # Float variable to store height in meters
is_student = True  # Boolean variable to indicate student status

# Printing each variable with appropriate message
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "meters")
print("Am I a student?", is_student)
print()

# Question 2: Type Checking
# Printing the data type of each variable using type() function
print("Data type of name:", type(name))
print("Data type of age:", type(age))
print("Data type of height:", type(height))
print("Data type of is_student:", type(is_student))
print()

# Part 2: Simple Operations with Variables                                          
print("Part#2\n")

# Question 1: Mathematical Operations
num1 = 15  # Integer variable
num2 = 7.5  # Float variable

# Performing mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Printing results of each operation
print("The sum of num1 and num2 is:", addition)
print("The difference of num1 and num2 is:", subtraction)
print("The product of num1 and num2 is:", multiplication)
print("The quotient of num1 divided by num2 is:", division)
print()

# Question 2: String Concatenation
first_name = "Behram"
last_name = "Saqlian"
full_name = first_name + " " + last_name  # Concatenating strings
print("Full name:", full_name)
print()

# Part 3: Working with User Input
print("Part#3\n")

# Question 1: User Input
# Prompting user for input
full_name = input("Please enter your full name: ")
age = int(input("Please enter your age: "))  # Converting input to integer
fav_number = float(input("Please enter your favorite number: "))  # Converting input to float

# Printing a message with all inputs
print("Hello", full_name + "! You are", age, "years old and your favorite number is", fav_number)
print()

# Question 2: Type Conversion
# Converting favorite number from float to integer
fav_number_int = int(fav_number)

# Printing both values with their types
print("Original favorite number:", fav_number, "- Type:", type(fav_number))
print("Converted favorite number:", fav_number_int, "- Type:", type(fav_number_int))
print()

# Part 4: Logical Operations
print("Part#4\n")

# Question 1: Boolean Expressions
is_sunny = True
is_weekend = False

# Creating boolean expression to check if both sunny and weekend
is_sunny_weekend = is_sunny and is_weekend

# Printing the result
print("Is it both sunny and weekend?", is_sunny_weekend)
print()

# Part 5: Challenge (Optional but Encouraged)
print("Part#5\n")

# Question 1: Data Type Conversion Challenge
a = "123"  # String
b = "45.67"  # String

# Converting to correct data types
a_int = int(a)  # Converting to integer
b_float = float(b)  # Converting to float

# Performing mathematical operation (addition)
result = a_int + b_float

# Printing the result
print("The result of adding", a_int, "and", b_float, "is:", result)