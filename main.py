# Input and Output
# Input allows users to enter data, and Output is used to display data
name = input("Enter your name: ")  # Taking input from the user
print("Hello, " + name + "!")  # Outputting a message to the user

# Variables
# Variables store data values. In Python, you don't need to declare variable types explicitly.
age = 25  # Assigning a value to a variable
height = 5.9  # Another variable storing a float value
print("Age:", age, "Height:", height)

# Keywords
# Keywords are reserved words that have special meaning in Python
# Example: 'if', 'else', 'elif', 'while', 'for', 'def', etc.

# Operators
# Operators are symbols that perform operations on variables and values
x = 10
y = 5
sum_result = x + y  # Addition
diff_result = x - y  # Subtraction
mul_result = x * y  # Multiplication
div_result = x / y  # Division
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Multiplication:", mul_result)
print("Division:", div_result)

# Data Types
# Python has several data types like int, float, string, list, etc.
num1 = 10  # Integer
num2 = 20.5  # Float
name = "Alice"  # String
is_student = True  # Boolean
students_list = ["John", "Alice", "Bob"]  # List
print("Integer:", num1, "Float:", num2, "String:", name, "Boolean:", is_student)
print("List of students:", students_list)

# Conditional Statements
# Conditional statements allow you to execute certain code based on conditions
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Elif example
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Python Loops
# Loops help you repeat actions in Python. There are two types: 'for' and 'while' loops

# 'For' loop
for i in range(5):  # Loop runs 5 times
    print("For loop iteration:", i)

# 'While' loop
count = 0
while count < 3:  # Loop will run while the condition is True
    print("While loop iteration:", count)
    count += 1  # Increment the count to avoid infinite loop