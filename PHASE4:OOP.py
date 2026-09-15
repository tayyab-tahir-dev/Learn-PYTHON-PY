                                  # <----------PHASE 4: OOPS---------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1) OOP in Python
# 2) Swift vs Python comparison
# 3) __init__
# 4) self
# 5) inheritance
# 6) polymorphism
# 7) abstraction
# 8) encapsulation
# 9) dataclass
# 10) property
# 11) magic methods

# - OOP--->

# INTERVIEW DEFINATION:
# OOP (Object-Oriented Programming) is a programming paradigm that organizes code using classes and objects.

# SIMPLE UNDERSTAND:
# OOP aik programming approach hai jisme hum program ko classes aur objects ki form mein organize karte hai.

# Core Concepts: Classes and Objects

# OOP
#  ↓
# Classes + Objects

# CLASS  =  A blueprint or template for creating objects.
# SIMPLE: 
# Ek aisa design/structure jo objects banane ke liye use hota hai.


# OBJECT =  An instance of a class containing real data.
# SIMPLE: 
# Class ka ek actual instance jisme asal data mojood hota hai.

# EXAMPLE:

# class Student:
#     pass

# student1 = Student()
# student2 = Student()

# print(student1)
# print(student2)

# EXPLANATION:

# class Student: → Student naam ki class / blueprint bana
# pass → Class ke andar abhi koi code nahi hai
# student1 = Student() → Student class ka pehla actual object/instance bana
# student2 = Student() → Student class ka doosra actual object/instance bana
# print(student1) → student1 object ko print karega
# print(student2) → student2 object ko print karega

                             #<----------ATTRIBUTE--------->

# - attribute--->

# INTERVIEW DEFINATION:
# An attribute is a variable that belongs to an object or class and stores its data.

# SIMPLE UNDERSTAND:
# Attribute woh variable hota hai jo object ya class ka data store karta hai.

# EXAMPLE:

# class student:
#     pass

# student1 = student()

# student1.name = "Tayyab"
# student1.age = 18
# student1.course = "Python"

# print(student1.name)
# print(student1.age)
# print(student1.course)


                               # <----------METHOD---------->

# - METHOD--->
# INTERVIEW DEFINATION:
# A method is a function defined inside a class that performs an action for an object.

# SIMPLE UNDERSTAND:
# Method aik function hota hai jo class ke andar define kiya jata hai aur object ka koi action perform karta hai.

# EXAMPLE:

# class Student:

#     def study(self):
#         print("Student is studying")


# student1 = Student()

# student1.study()



# yahan:
# def study(self): method hai.

# Aur:

# student1.study() method ko call kar raha hai.


# EXAMPLE WITH ATTIRBUTE:


# class student:

#     def study(self):
#         print("Student is studying")


# student1 = student()

# student1.name = "Tayyab"

# print(student1.name)
# student1.study()


# YHA KYA HO RHA HAI: 

                      # class Student
                      #       ↓
                      #   Blueprint
                      #       ↓
                      # Student()
                      #       ↓
                      # Actual Object
                      #       ↓
                      #  student1
                      #       ↓
                      # ┌─────────────────────┐
                      # │ Student Object      │
                      # │                     │
                      # │ name = "Tayyab"     │
                      # │                     │
                      # │ study()             │
                      # └─────────────────────┘
                      #       ↓
                      # student1.name
                      #       ↓
                      # "Tayyab"
                      
                      # student1.study()
                      #       ↓
                      # "Student is studying"

# 🤖 AI Engineering Example

              
# class AIModel:

#     def generate_response(self, prompt):
#         # yahan future mein LLM API call ho sakti hai
#         print("Generating response for:", prompt)


# model = AIModel()

# model.generate_response("Explain Python OOP")


# IMPORTANT:

# AI Engineering mein:
# Real project mein print() ki jagah yahan LLM API call ho sakti hai, jo prompt ko AI model ko bhej kar response return karegi.