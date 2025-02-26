# Python Beginner Topics: Input, Variables, Operators, Conditional Statements, and Loops

This Python script demonstrates basic programming concepts including input/output, variables, keywords, operators, data types, conditional statements, and loops. It’s perfect for beginners learning the fundamentals of Python.

## Features

- **Input and Output**: Learn how to take input from users and display output.
- **Variables**: Understanding how to assign values to variables and use them in Python.
- **Keywords**: Introduction to Python reserved keywords like `if`, `else`, and more.
- **Operators**: Perform basic mathematical operations using operators.
- **Data Types**: Work with different data types like integers, floats, strings, booleans, and lists.
- **Conditional Statements**: Make decisions in your code using `if`, `elif`, and `else`.
- **Loops**: Learn how to repeat actions using `for` and `while` loops.

## Code Overview

This script covers the following topics:

1. **Input and Output**: 
   - Takes user input and displays it using `input()` and `print()`.

2. **Variables**: 
   - Shows how to assign values to variables, including different types like integers, floats, strings, and booleans.

3. **Operators**:
   - Performs basic arithmetic operations like addition, subtraction, multiplication, and division.

4. **Data Types**:
   - Introduces different data types such as integers, floats, strings, booleans, and lists.

5. **Conditional Statements**:
   - Uses `if`, `elif`, and `else` to check conditions and execute code based on specific criteria.

6. **Loops**:
   - Demonstrates how to use `for` and `while` loops to repeat actions multiple times.

## Example Code

```python
# Input and Output
name = input("Enter your name: ")  # Taking input from the user
print("Hello, " + name + "!")  # Outputting a message to the user

# Variables
age = 25
height = 5.9
print("Age:", age, "Height:", height)

# Operators
x = 10
y = 5
sum_result = x + y
print("Sum:", sum_result)

# Data Types
num1 = 10  # Integer
num2 = 20.5  # Float
name = "Alice"  # String
is_student = True  # Boolean
students_list = ["John", "Alice", "Bob"]  # List
print("Integer:", num1, "Float:", num2, "String:", name, "Boolean:", is_student)

# Conditional Statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Python Loops
for i in range(5):  # Loop runs 5 times
    print("For loop iteration:", i)

count = 0
while count < 3:  # Loop runs while count is less than 3
    print("While loop iteration:", count)
    count += 1