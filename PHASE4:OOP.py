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


                            # <----------TYPES OF METHODS IN OOP---------->


# - METHODS--->
# 1) INSTANCE METHOD:

# INTERVIEW DEFINATION:
# An instance method is a method that works with the data of a specific object (instance) and takes self as its first parameter.

# SIMPLE UNDERSTAND:
# Instance method woh method hota hai jo kisi specific object ke data ke saath kaam karta hai aur uska pehla parameter self hota hai.

# ISKO "INSTANCE" Q KEHTAY HAI:

# Class → Blueprint
# Object → Instance

# Isliye:

# Instance Method = Object ke saath kaam karne wala method


# EXAMPLE:
# WITH MULTIPLE OBJECTS:

# class student:

#     def introduce(self):
#         print("My name is", self.name)

# student1 = student()
# student1.name = "Tayyab:"

# student2 = student()
# student2.name = "Ali:"

# student1.introduce()
# student2.introduce()


# Isi liye instance method har object ke apne data ke saath kaam kar sakta hai.

# 🤖 AI Engineering Example
# AI project mein:

# class AIModel():

#     def generate_response1(self):
#         print("Generating response by model 1....")


#     def generate_response2(self):
#         print("Generating response by model 2....")


# model1 = AIModel()
# model2 = AIModel()

# model1.generate_response1()
# model2.generate_response2()


                                        # IMPORTANT POINTS:

                                  # Instance Method
                                  #       ↓
                                  # Object ke saath kaam karta hai
                                  #       ↓
                                  # self as first parameter
                                  #       ↓
                                  # Object ke attributes access kar sakta hai

                                

# - METHODS--->
# 2) CLASS METHOD:
# INTERVIEW DEFINATION:
# A class method is a method that works with the class itself rather than a specific object.

# SIMPLE UNDERSTAND:
# Class method kisi specific object ke bajaye poori class ke saath kaam karta hai.

# Iski Pehchan kaise hoti hai?

# Class method mein:
# @classmethod
# likha hota hai.
# Aur iska first parameter normally:
# cls

# MAIN DIFFERENCE:

# Instance Method
# → specific object ke data ke saath kaam

# Class Method
# → class ke data/behavior ke saath kaam

# EXAMPLE:

# class Student:

#     @classmethod
#     def school_name(cls):
#         print("ABC School")

# Student.school_name()


# Yahan:
# @classmethod
# Python ko batata hai ke school_name() class method hai.

# cls kya hai:

# Class Method
#       ↓
#      cls
#       ↓
#      class

# cls ka matlab roughly:
# jis class se method related hai, us class ko refer karo.

# SIMPLE EXAMPLE:

# class Student:

#     @classmethod
#     def show_school(cls):
#         print("ABC School")

# Student.show_school()


# REAL AI EXAMPLE:


# class AIModel:

#     model_type = "LLM"

#     @classmethod
#     def show_model_type(cls):
#         print(cls.model_type)


# AIModel.show_model_type()

# # BRIEFLY EXPLANATION:
# class AIModel:

#     model_type = "LLM"
# AIModel → class
# model_type → class attribute
# "LLM" → uski value
# @classmethod
# def show_model_type(cls):
#     print(cls.model_type)
# @classmethod → batata hai ke show_model_type() Class Method hai.
# cls → poori class AIModel ko refer karta hai.
# cls.model_type → class ka model_type access karta hai.

# Phir:

# AIModel.show_model_type()
# Yahan object banane ki zaroorat nahi. Direct class ke through method call ho raha hai.



# - METHODS--->
# 3) STATIC METHOD:

# INTERVIEW DEFINATION:
# A static method is a method that does not depend on a specific object or class data.

# SIMPLE UNDERSTAND:
# Static method kisi specific object ya class ke data par depend nahi karta.

# Static method kis cheez par depend karta hai?
# Jo arguments/parameters usko diye jate hain, un par.

# Iski pehchan
# Static method ke upar:
# @staticmethod


# Static Method mein self aur cls nahi hota:

# Instance Method → self → Object
# Class Method    → cls  → Class
# Static Method   → no self/cls

# SIMPLE EXAMPLE:

# class Calculator:

#       @staticmethod
#       def add(a, b):
#             return a + b


# print(Calculator.add(10, 20))


# REAL AI EXAMPLE:

# class AIHelper:

#     @staticmethod
#     def count_words(text):
#         return len(text.split())

# text = "Python is useful for AI Engineering"

# print(AIHelper.count_words(text))

# LOGIC:

                             # "Python is useful for AI Engineering"
                                          #    ↓
                                    #     text.split()
                                          #    ↓
                         # ["Python", "is", "useful", "for", "AI", "Engineering"]
                                          #    ↓
                                          #  len()
                                          #    ↓
                                          #    6
                                          #    ↓
                                          # return 6
                                          #    ↓
                                          # print(6)

# IMPORTANT:

# Instance Method
# → self
# → object ke data ke saath kaam

# Class Method
# → cls
# → class ke data ke saath kaam

# Static Method
# → no self
# → no cls
# → independent operation



                                      # <----------__init__---------->


# INTERVIEW DEFINATION:
# __init__ is a special method that initializes an object's attributes when the object is created.

# SIMPLE UNDERSTAND:
# __init__ aik special method hai jo object create hote waqt uske attributes ko initialize/set karta hai.

# INKI PEHCHAN:
# DOUBLE UNDERSCORES: 
# __init__

# IMPORTANT:
# __init__
# → special method:
# → object creation ke waqt initialization ke liye run hota hai:
# → object ke attributes set karta hai:


# EXAMPLE:

# class student:

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course


# student1 = student("Tayyab", 18, "Python")

# print(student1.name)
# print(student1.age)
# print(student1.course)


# 🤖 AI Engineering Example
# AI Engineering mein hum kisi AI model ka object bana sakte hai:

# class AIModel:

#     def __init__(self, model_name, provider):
#         self.model_name = model_name
#         self.provider = provider


# model = AIModel("GEMINI", "GOOGLE")

# print("MODEL_NAME =", model.model_name)
# print("PROVIDER =", model.provider)

# Real project mein isi pattern se object ke andar model configuration, API client, settings waghera initialize ki ja sakti hain.



                                      # <----------SELF---------->

# - SELF-->

# INTERVIEW DEFINATION:
# self refers to the current object (instance) on which an instance method is being called.

# SIMPLE UNDERSTAND:
# self us current object ko refer karta hai jis object ke through method call kiya ja raha hota hai.

# SIMPLEST EXAMPLE:

# class student:

#     def study(self):
#         print("Studying")


# student1 = student()
# student1.study()


# yahan:

# student1.study()

# student1 object ne study() method call kiya.

# Isliye method ke andar:

# self

# student1 ko refer karega.

                                            # SIMPLE:
                                            
                                            # student1.study()
                                            #        ↓
                                            #      self
                                            #        ↓
                                            #    student1

# IMPORTANT:

# self → current object

# self.name → current object ka name attribute
# self.age  → current object ka age attribute
# Instance method mein self first parameter hota hai:

# 🧠 One-line Logic

# Object method call karta hai
#         ↓
# self us object ko refer karta hai
#         ↓
# self.attribute us object ka attribute access karta hai


                                      # <----------OOP 4 PILLARS---------->

# - OOP 4 PILLARS--->
# OOP ke 4 pillars woh 4 basic concepts hain jin par Object-Oriented Programming ka structure based hota hai.

# 1) Inheritance
# 2) Polymorphism
# 3) Encapsulation
# 4) Abstract

# 1) - Inheritance-->
# INTERVIEW DEFINATION:
# Inheritance is an OOP concept in which a child class inherits attributes and methods from a parent class.

# SIMPLE UNDERSTAND:
# Inheritance mein child class, parent class ke attributes aur methods ko inherit/reuse karti hai.

# IMPORTANT:
# CHILD PARENT KI CHIZAY LE SKTA HAI
# LEKIN:
# LEKIN PARENT CHILD KI NHI

# SIMPLE EXAMPLE:

# class sleeping:

#     def sleep(self):
#         print("I am sleeping")


# class awake(sleeping):

#     def woke(self):
#        print("I am awake now")


# awake1 = awake()

# awake1.sleep()
# awake1.woke()


# REAL AI EXAMPLE:

# class AIModel:

#     def generate_response(self):
#         print("GENERATING RESPONSE")


# class GeminiModel(AIModel):

#     def model_info(self):
#         print("THIS IS GEMINI MODEL")


# model = GeminiModel()

# model.generate_response()
# model.model_info()

# Yahan GeminiModel ne AIModel ka generate_response() method inherit kiya.

# AI Engineering mein inheritance useful ho sakti hai jab multiple AI models mein kuch common functionality ho aur hum us common code ko baar baar repeat nahi karna chahte.