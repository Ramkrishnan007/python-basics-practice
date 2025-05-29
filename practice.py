course = "Ramkrishnan"
print(len(course))  # length of the string
print(course[-1])
print(course[0:3])

Name = "Ram\"krishnan"  # name with a quote
print(Name)
Name_user = "Ram\nkrishnan"  # name with a quote
print(Name_user)

var1 = input("Enter your firstname: ")
var2 = input("Enter your lastname: ")
var = f"{var1} {var2}"# name with a space using f-string
print(var)
var3 = f"{len(var1)} {2+2}"
print(var3)  # length of first name and a simple calculation

# String methods
MyName = "  ramkrishnan"
print(MyName.upper())  # convert to uppercase
print(MyName.lower())  # convert to lowercase
print(MyName) # original string remains unchanged
print(MyName.title()) # convert to title case
print (MyName.strip())  # remove leading and trailing spaces
print(MyName.find("k"))  # find the index of 'k'
print(MyName.replace("ram", "R"))  # replace 'Ram' with 'R'
print("ram" in MyName)  # check if 'ram' is in the string
print("ram" not in MyName)  # check if 'ram' is not in the string

# Numbers -> integer and float,complex numbers
num1 = 10  # integer
num2 = 3.14  # float
num3 = 1 + 2j  # complex number
print(1+3)
print(10-8)
print(10*8)
print(10/3)  # division
print(10//3)  # floor division
print(10%3)  # modulus
print(10**3)  # exponentiation

x = 10
x = x + 5  # increment x by 5
x +=5 # another way to increment x by 5

# Working with numbers

print (round(3.14159))  # round to 2 decimal places
print (abs(-2.8)) # absolute value
import math # math module for advanced math functions
print (math.ceil(2.2))  # round up to the nearest integer

# type conversion

input_String = input("Enter a number:")
print(type(input_String))  # this will show that input is a string
# output_int = input_String+1 # this will cause an error because input is a string
# print(output_int)
# To fix the error, we need to convert the input string to an integer
output_int = int(input_String) + 1  # convert string to integer
print(output_int)  # now this will work correctly
print(f"input_String is: {input_String}, and its type is: {output_int} and its type is: {type(output_int)}")

# falsy
# falsy values in Python
falsy_values = [0, 0.0, "", None, [], {}, set(),1, "False", "0", True, "1", "Hello", " ", "0.0"]
for value in falsy_values:
    if not value:  # checks if the value is falsy
        print(f"{value} is falsy")
    else:
        print(f"{value} is truthy")
# This will print whether each value is falsy or truthy
# Note: In Python, empty strings, zero values, None, empty collections (like lists, sets, and dictionaries) are considered falsy.

#comparison operators
# Comparison operators in Python
comparison_operators = [
    (5, 3, "=="),  # equal to
    (5, 3, "!="),  # not equal to
    (5, 3, ">"),   # greater than
    (5, 3, "<"),   # less than
    (5, 3, ">="),  # greater than or equal to
    (5, 3, "<=")   # less than or equal to
]
for a, b, op in comparison_operators:
    if op == "==":
        result = a == b
    elif op == "!=":
        result = a != b
    elif op == ">":
        result = a > b
    elif op == "<":
        result = a < b
    elif op == ">=":
        result = a >= b
    elif op == "<=":
        result = a <= b
    print(f"{a} {op} {b} : {result}")
# This will print the result of each comparison operation
# Logical operators
# Logical operators in Python
logical_operators = [
    (True, False, "and"),  # logical AND
    (True, False, "or"),   # logical OR
    (True, False, "not")   # logical NOT
]
for a, b, op in logical_operators:
    if op == "and":
        result = a and b
    elif op == "or":
        result = a or b
    elif op == "not":
        result = not a
    print(f"{a} {op} {b if op != 'not' else ''} : {result}")
# This will print the result of each logical operation

# conditional statements

temperature = input("Enter the temperature today")  # example temperature value
temperature = int(temperature)  # convert input to integer
# Check the temperature and print a message accordingly
if temperature > 30:
    print("It's a hot day")
elif temperature < 20:
    print("It's a cold day")
else:
    print("It's a pleasant day")
# This will print a message based on the temperature value

# Ternary operator
# Ternary operator in Python
age = input("Enter your age: ")  # example age value
age = int(age)  # convert input to integer

message = "You are an adult" if age >= 18 else "You are a minor"
print(message)  # This will print the message based on the age value
# This is a simple way to use the ternary operator in Python


# Chaining Comparison Operators
# Chaining comparison operators in Python
def check_age(age):
    if 18 <= age < 65:
        return "You are an adult"
    elif age < 18:
        return "You are a minor"
    else:
        return "You are a senior citizen"


# for loop
for number in range(3):
    print("Message", number+1)  # This will print "Message 1", "Message 2", "Message 3"

for number in range (1, 4):
    print("Message", number)  # This will print "Message 1", "Message 2", "Message 3"
    
#for else
success = True  # Example condition
for number in range(3):
    print("Message")
    if success:
        print("Success!")
        break
else:
    print("No success after all iterations")

# nested for loop

for i in range (5):
    for j in range(7):
        print(f"Outer loop {i}, Inner loop {j}")  # This will print combinations of outer and inner loop indices   
        
# Iterables

print(type(10)) # int
print(type(range(10))) # range object

for x in range(10):
    print(x)  # This will print numbers from 0 to 9

# Iterating over a string
for char in "Hello":
    print(char)  # This will print each character in the string "Hello"


for x in [1,2,3,4]:
    print(x) # This will print each element in the list [1, 2, 3, 4]

# while loop

num = 100 

while num >0 :
    print(num)
    num //=2 # This will print the value of num and then divide it by 2 until num is less than or equal to 0

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)  # This will print the command entered by the user until "quit" is entered

# task-1

number = int(input("Enter a number: "))
if number % 2 ==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# task-2
n = int(input("Enter a number of elements in the array:"))
even_count = 0
odd_count = 0
for i in range (n):
    num = int (input(f"Enter element {i+1}: "))
    if i % 2 ==0:
        even_count +=1
    else:
        odd_count +=1
print(f"Number of even indexed elements: {even_count}")
print(f"Number of odd indexed elements: {odd_count}")
# This will count the number of even and odd indexed elements in the array

# functions

def greet():
    print("Hello, welcome to the Python course!")  # This function prints a greeting message
    print("This is a simple function without parameters or return value")  # Additional message  
greet()  # Calling the greet function to execute its code

# arguments and parameters

def greet(first_name,last_name):
    print(f"Hello, {first_name} {last_name}! Welcome to the Python course!")  # This function prints a greeting message with first and last name
    print("This function takes two parameters: first_name and last_name")  # Additional message

first_name = input("Enter your first name: ")  # Taking first name input from the user
last_name = input("Enter your last name: ")  # Taking last name input from the user
greet(first_name, last_name)  # Calling the greet function with user inputs as arguments

#types of functions 

#1- perform a task
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course!")  # This function prints a greeting message with the user's name
#2- return a value
def add_numbers(a, b):
    return a + b  # This function takes two numbers as parameters and returns their sum
#3- perform a task and return a value
def calculate_area(length, width):
    area = length * width  # This function calculates the area of a rectangle
    print(f"The area of the rectangle is: {area}")  # Prints the calculated area
    return area  # Returns the area value

def great (name):
    print(f"Hello, {name}! Welcome to the Python course!")  # This function prints a greeting message with the user's name

print(great("Ramkrishnan"))  
# This will print "Hello, Ramkrishnan! Welcome to the Python course!" and return None since the function does not have a return statement because it is a void function

# keyword arguments

def increment(number, by):
    return number + by  # This function increments the number by the specified value (default is 1)

# incremented_value = increment(10, by=5)  # Calling the function with keyword argument 'by'
# print(incremented_value)  # This will print the incremented value, which is 15 in this case
print(increment(10, by=5))  # This will print the incremented value, which is 15 in this case same as above but without storing in a variable and printing it directly simply with keyword argument

# Default arguments
def increment(number, by=1):
        return number + by  # This function increments the number by the specified value (default is 1)
print(increment(10))  # Calling the function with default argument, this will print 11
print(increment(10, by=5))  # Calling the function with keyword argument 'by', this will print 15


#args,wait,what

def multiply(*numbers):
    total  = 1  # Initialize total to 1 for multiplication
    for number in numbers:
        total *= number  # Multiply each number with the total
    return total  # Return the final product
# Example usage
numbers = [2, 3, 4]  # List of numbers to multiply  
for number in numbers:
    print(number)

result = multiply(*numbers)  # Unpacking the list into the function
print(f"The product of {numbers} is: {result}")  # This will print the product of the numbers in the list
# This will print "The product of [2, 3, 4] is: 24"
# This function takes a variable number of arguments and multiplies them together
#end of the code
# Note: The * operator is used to unpack the list into individual arguments for the function