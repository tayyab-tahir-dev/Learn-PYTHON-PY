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


                           # <----------*args---------->

# Definition
# *args: *args allows a function to accept any number of positional arguments.

# SIMPLE UNDERSTAND:
# *args function ko allow karta hai ke woh jitni bhi positional values receive kar sake.

# Important:
# * he batata hai ke function multiple positional arguments accept karega. args sirf 
# variable ka naam hai.

# *args kay andar jo multiple positional arguments aate hain, function ke andar woh tuple ki form mein 
# milte hain.

# EXAMPLE:
# 1).

# def add(*args):
#     print(numbers)

# add(10, 20, 40, 30, 40)

# 2).

# 0 argument bi de sktay hai.

# def show(*args):
#     print(args)

# show()

# 3).

# def show(*args):
#     print(args)

# show("Tayyab", "Ali", "Ahmad")

# 4).

# def total(*numbers):
#     print(sum(numbers))

# total(10, 20, 40)


                  # <----------POSITIONAL ARGUMENTS---------->

# DFINATION:
# Positional arguments: Arguments are passed to a function based on their position or order.

# SIMPLE UNDERSTAND:
# Positional arguments mein values jis order mein pass hoti hain, woh usi order mein function ke 
# parameters ko assign hoti hain.
# EXAMPLE:

# 1).
# def student(name, age):
#     print(name)
#     print(age)

# student("Tayyab", 18)

# ---EXPLANATION---

# "Tayyab" → name
# 18       → age

# Kyun?

# Kyun ke "Tayyab" first position par hai aur name bhi first parameter hai.
# 18 second position par hai aur age second parameter hai.

# 2).
# ORDER CHANGE:

# def student(name, age):
#     print(name)
#     print(age)

# student(18, "Tayyab")

# 3).

# def introduce(name, age, course):
#     print("name:", name)
#     print("age:", age)
#     print("course:", course)

# introduce("Tayyab", 18, "Python")


                        # <----------KEYWORD ARGUMENTS---------->


# DEFINATION:
# Keyword arguments: Arguments passed to a function by explicitly specifying the parameter name.

# SIMPLE UNDERSTAND:
# Keyword argument mein hum value ke saath parameter ka naam bhi likhte hain, is liye order 
# important nahi rehta.
# EXAMPLE:

# 1).

# def student(name, age, rollnum):
#     print("Name:", name)
#     print("Age:", age)
#     print("Roll Num:", rollnum)

# student(rollnum=2293, name="Tayyab", age=18)

# EXPLANATION:
# Yha pr position/order matter nhi krta because ython parameter ke naam dekh kar value assign 
# karta hai, position nahi.
