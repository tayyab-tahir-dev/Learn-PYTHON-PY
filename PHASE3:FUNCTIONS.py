                        # <--------PHASE 3: FUNCTIONS-------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1) Function
# 2) Parameters
# 3) *args
# 4) Positional Arguments
# 5) Keyword Arguments
# 6) **kwargs
# 7) Lambda
# 8) Nested Functions
# 9) Closures
# 10) Decorators — Introduction
# 11) Real AI Examples

# - FUNCTION--->

# Definition:
# Function: A function is a reusable block of code that performs a specific task when it is called.

# SIMPLE UNDERSTAND:
# Function code ka reusable block hota hai jo ek specific kaam karta hai jab usay call kiya jata 
# hai.

# EXAMPLES:

# 1)-

# def greet():
#     print("Hello World")

# greet()

# def     → function banane ka keyword
# greet   → function ka naam
# ()      → parameters/arguments ki jagah/abhi empty hain
# :       → function body start hone ka signal
# print() → function ka kaam
# greet() → function ko call karne ka tarika

# def greet() function ka woh hissa hai jahan hum function ko define karte hain aur uska naam 
# batate hain.

# print("Hello World")
# yeh function body hai.

# Simple rule:
# : se pehle = function ki heading
# : ke baad indented code = function ki body

# Define = function banana
# Call = function ko chalana

# 2)-

# def greet(name):
#     print("Hello", name)

# greet("Tayyab")

# 3)-

# def welcome():
#     print("Learning Python")

# welcome()
# welcome()
# welcome()


                         # <----------PARAMETERS---------->

# DEFINATION:
# Parameter: A parameter is a variable defined inside a function's parentheses that receives a 
# value when the function is called.

# SIMPLE UNDERSTAND:
# Parameter function ke () ke andar banaya gaya variable hota hai jo function call hone par value 
# receive karta hai.

# EXAMPLE:

# 1)-

# def greet(name):
#     print("Hello", name)

# greet("Tayyab")

# Yha name PARAMETER hai.
# "Tayyab" value hai jo name parameter mein receive hui.

# 2)-
# Multiple Parameters:
# Function mein multiple parameters bhi ho sakte hain.

# def introduce(name, age):
#     print("My name is", name)
#     print("I am", age, "years old")

# introduce("Tayyab", 18)  

# 3)-

# def student_info(name, course):
#     print("Name:", name)
#     print("course:", course )

# student_info("Tayyab", "Python")