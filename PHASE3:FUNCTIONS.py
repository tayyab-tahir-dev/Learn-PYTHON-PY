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

# *args ke andar data tuple ki form mein hota hai, isliye tuple ke ye operations *args par 
# bhi kar sakte ho:

# JASAY YEH SUB OPERATIONS:
# def student(*args):
#     print(args[0])          # indexing / access
#     print(args[1:3])        # slicing
#     print(len(args))        # length
#     print(18 in args)       # membership
#     print(args.count(18))   # count
#     print(args.index(18))   # index

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
#     print("name", name)
#     print("Age:", age)
#     print("Roll Num:", rollnum)

# student(rollnum=2293, name="Tayyab", age=18)

# EXPLANATION:
# Yha pr position/order matter nhi krta because Python parameter ke naam dekh kar value assign 
# karta hai, position nahi.


                             # <----------**kwarg---------->

                            
# DEFINATION:
# **kwargs allows a function to accept any number of keyword arguments.

# SIMPLE UNDERSTAND:
# **kwargs function ko kisi bhi number mein keyword arguments receive karne ki ability deta hai.

# Function name ke andar saari values dictionary ki form mein aati hain.

# EXAMPLE:
# 1).

# def details(**kwargs):
#     print(kwargs)

# details(name="Tayyab", age=18, course="Python")


# | `*args`              | `**kwargs`              |
# | -------------------- | ----------------------- |
# | Positional arguments | Keyword arguments       |
# | Tuple mein collect   | Dictionary mein collect |
# | `10, 20, 30`         | `name="Tayyab", age=18` |


# IMPORTANT:
# **kwargs ke andar jo data collect hota hai, woh dictionary hi hota hai. Isliye dictionary ke 
# methods/operations use kar sakte hai.

# **kwargs khud dictionary nahi, balki keyword arguments ko dictionary mein collect karta hai.

# JASAY YEH SUB OPERATIONS:
# def student(**info):
#     print(info["name"])       # access
#     print(info.keys())        # keys
#     print(info.values())      # values
#     print(info.items())       # key-value pairs

# 2). VALUES KO ACCESS KRNA DICTIONARY KI TARAH:

# def profile(**info):
#     print(info["name"])
#     print(info["user_name"])

# profile(name="Tayyab", user_name="tayya9439b")



                               # <----------LAMBDA---------->


# DEFINATION
# Lambda: A lambda is a small anonymous function written in a single expression.

# SIMPLE UNDERSTAND:
# Lambda ek chhota function hota hai jiska usually koi naam nahi hota, aur isay ek hi expression 
# mein likha jata hai

# Normal Function
# def add(a, b):
#     return a + b

# print(add(10, 30))


# Same thing with Lambda
# add = lambda a, b: a + b

# print(add(10, 30))


# Lambda ka structure
# lambda parameters: expression

# EXAMPLE:

# square = lambda number: number * number
# print(square(5))

# Yahan:

# lambda          → lambda function banane ka keyword
# number          → parameter
# number * number → expression
# result automatically return hota hai

# Important Point

# Lambda mein return keyword nahi likhte:
# square = lambda x: x * x
# x * x ka result automatically return hota hai.

# Lambda kab useful hai?
# Jab hamay bohat chhota aur simple function temporarily banana ho.

# EXAMPLE:

# double = lambda x: x * 2
# print(double(10))

# multiply = lambda a, b: a * b
# print(multiply(5, 4))

# cube = lambda x: x * x * x
# print(cube(3))




                                # <----------NESTED FUNCTION---------->


# DEFINATION:
# Nested Function: A function defined inside another function is called a nested function.

# SIMPLE UNDERSTAND:
# Jab hum ek function ke andar doosra function define karte hain, usay nested function kehte hain.

# BASIC EXAMPLE:

# def outer():

#     def inner():
#         print("Hello from inner function")

#     inner()

# outer()


# Yahan:

# def outer():
# outer → outer function

# Aur:

# def inner():
# inner → nested/inner function

# Logic

# Pehle:
# outer()
# outer() execute hota hai.

# Uske andar:
# inner()
# inner() call hota hai.

# Isliye "Hello from inner function" print hota hai.

# EXAMPLE:
# def student():

#     def info():
#         print("Name:", "Tayyab")
#         print("Course:", "Python")

#     info()

# student()

# Important Point

# Inner function ko normally outer function ke bahar directly call nahi kar sakte, kyun ke woh 
# outer function ke andar define hua hai.

# Remember:

# Outer function ke andar inner function define hota hai.
# Inner function ko outer function ke andar call kar sakte hain.



                                # <----------CLOSER---------->

# DEFINATION:
# Closure: A closure is a function that remembers and can access variables from its enclosing 
# function even after the enclosing function has finished executing.

# SIMPLE UNDERSTAND:
# Closure mai inner function apne outer function ke variables ko yaad rakhta hai, chahe outer 
# function ka execution khatam hi kyun na ho.

# EXAMPLES:
# 1)

# def outer_function(msg):
#     # Yeh outer function ka variable hai
#     greeting = msg 

#     def inner_function():
#         # Inner function outer variable ko use kar raha hai
#         print(greeting) 
        
#     # Outer function ne inner function ko return kar diya
#     return inner_function

# # Humne outer function ko call kiya aur result ek variable mein save kar liya
# my_closure = outer_function("Hello Python!")

# # Ab 'outer_function' khatam ho chuka hai, lekin...
# # Jab hum 'my_closure' ko call karenge:
# my_closure()


# 2)

# def greeting(message):

#     def say():
#         print(message)

#     return say


# hello = greeting("Hello Tayyab")
# hello()


                         # <----------DECORATOR----------->

# DEFINATION:
# Decorator: A decorator is a function that modifies or extends the behavior of another function 
# without changing its original code.

# SIMPLE UNDERSTAND:
# Decorator aik function hota hai jo doosre function ke behavior mein extra functionality add 
# karta hai, bina us function ka original code change kiye.

# SYNTAX:
# Python mein decorator ko commonly @ ke saath likhte hain:

# def decorator(function):

#     def wrapper():
#         print("Before function")
#         function()
#         print("After function")

#     return wrapper


# @decorator
# def greet():
#     print("Hello Tayyab")


# greet()

# EXMAPLE:
# 1)

# def my_decorator(function):

#     def wrapper():
#         print("Starting...")
#         function()
#         print("Finished...")

#     return wrapper

# @my_decorator
# def task():
#     print("Python task running")


# task()


                 # <----------------REAL AI EXAMPLES-------->


# EXAMPLE 1 — AI Prompt Function:
# NORMAL FUNCTION.


# def  create_prompt(question):
#     prompt = f"Answer this question clearly: {question}"
#     return prompt

# result = create_prompt("What is Python")
# print(result)


# YHA EXACT KYA HO RHA HAI:

# "What is Python?"
#         ↓
#     question
#         ↓
#     prompt banta hai
#         ↓
#     return prompt
#         ↓
#      result
#         ↓
#     print(result)

