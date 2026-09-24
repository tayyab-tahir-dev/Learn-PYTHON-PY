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



# - SUPER-->

# super()
# SIMPLE UNDERSTAND:
# super() ka use child class ke andar parent class ke methods ko access/call karne ke liye hota hai.

# EXAMPLE:

# class Animal:

#     def speak(self):
#         print("Animal is speaking")


# class Dog(Animal):
#      def speak(self):
#          super().speak()
#          print("Dog is barking")


# dog1 = Dog()

# dog1.speak()

# YHA KYA HUA:

# Yahan kya hua?

# Dog ne speak() method ko override kiya.

# def speak(self):

# Ab agar hum:

# dog1.speak()

# karenge, to normally Dog ka speak() chalega.

# Lekin:

# super().speak()

# ka matlab hai:

# Parent class ka speak() method chalao.

# Isliye pehle:

# Animal is speaking

# phir:

# Dog is barking


# super() with __init__
# Ye inheritance mein bohat important hai:

# class Animal:

#     def __init__(self, name):
#       self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#        super().__init__(name)
#        self.breed = breed


# dog1 = Dog("Tommy", "German Shepherd")       

# print(dog1.name)
# print(dog1.breed)


# LOGIC:

                                    #     Dog object bana
                                    #             ↓
                                    #     Dog.__init__() call hua
                                    #             ↓
                                    #     name = "Tommy"
                                    #     breed = "German Shepherd"
                                    #             ↓
                                    #     super().__init__(name)
                                    #             ↓
                                    #     Animal.__init__("Tommy")
                                    #             ↓
                                    #     self.name = "Tommy"
                                    #             ↓
                                    #     self.breed = "German Shepherd"


# Important Difference

# Inheritance:

# Child parent se functionality inherit karta hai.

# super():

# Child ke andar parent ki functionality ko specifically call/access karta hai.

# Parent Class
# Isko kaha jata hai:

# Parent Class
# Base Class
# Super Class

# Child Class
# Isko kaha jata hai:

# Child Class
# Derived Class
# Sub Class



# - Method Overriding-->
# Method Overriding. Ye super() ke baad naturally aata hai.

# Method overriding mein child class parent ke existing method ko apne tareeqe se dobara define karti hai.

# SIMPLE UNDERSTAND:
# Method ka name same, lekin code/implementation alag.

# REAL AI EXAMPLE:

# class AIModel:

#     def generate_response(self):
#         print("Generating a response")


# class GeminiModel(AIModel):

#     def generate_response(self):
#          print("Generating response using Gemini")


# class GPTModel(AIModel):

#     def generate_response(self):
#          print("Generating response using GPT")


# ai = AIModel()
# gemini = GeminiModel()
# gpt = GPTModel()


# ai.generate_response()
# gemini.generate_response()
# gpt.generate_response()




# 2) - Polymorphism--->

# INTERVIEW DEFINATION:
# Polymorphism is the ability of different objects to respond to the same method or interface in different ways.

# SIMPLE UNDERSTAND:
# Polymorphism ka matlab hai ke different objects same method ko apne apne tareeqe se perform kar sakte hain.

# SIMPLE EXAMPLE:

# class Dog:

#     def speak(self):
#         print("DOG BARKS")


# class Cat:

#       def speak(self):
#            print("CAT MEOWS")


# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()

# Logic

# Dono objects ke paas same method name hai:

# speak()

# Lekin:

# dog.speak() → Dog ka behavior
# cat.speak() → Cat ka behavior

# Yani same method name, different behavior.

# Isi ko polymorphism kehte hain.

# Real Python Example

# Hum ek function bana sakte hain:

# def make_sound(animal):
#     animal.speak()


# make_sound(dog)
# make_sound(cat)

# Function ko farq nahi pad raha ke object Dog hai ya Cat.

# Bas usay pata hai ke object ke paas speak() method hona chahiye.


# REAL AI EXAMPLE:

# class GeminiModel:

#     def generate(self):
#         print("Response from Gemini")


# class GPTModel:

#     def generate(self):
#       print("Response from GPT")



# def run_model(model):
#     model.generate()


# gemini = GeminiModel()
# gpt = GPTModel()

# run_model(gemini)
# run_model(gpt)



# 3) - Encapsulation-->

# INTERVIEW DEFINATION:
# Encapsulation is the OOP concept of bundling data and methods together in a class and controlling access to that data.

# SIMPLE UNDERSTAND:
# Encapsulation ka matlab hai data (variables) aur us par kaam karne wale methods (functions) ko ek class mein rakhna aur data ka access control karna.

# ONE LINE:

# Encapsulation = Data + Methods ko class mein bundle karna + data ke access ko control karna.

# SIMPLE EXAMPLE:

# class BankAccount:

#     def __init__(self, balance):
#        self.__balance = balance

#     def get_balance(self):
#        return self.__balance

#     def deposit(self, amount):
#        self.__balance += amount


# account = BankAccount(1000)

# print(account.get_balance())

# account.deposit(1500)

# print(account.get_balance())


# REAL AI EXAMPLE:

# class AIModel:

#     def __init__(self,  api_key):
#         self.__api_key = api_key

#     def generate(self, prompt):
#         print("GENERATING RESPONSE....")

# model = AIModel("abc123")

# model.generate("Hello")



# self.__api_key
# ke through class ke andar controlled rakha gaya hai.

# Note: Python mein __name strict security/private variable nahi hota; ye mainly name mangling ke through direct access ko discourage/control karta hai.



# 4) - Abstraction--->

# INTERVIEW DEFINATION:
# Abstraction is the OOP concept of hiding implementation details and exposing only the essential functionality.

# SIMPLE UNDERSTAND:
# Abstraction ka matlab hai internal/complex implementation ko hide karna aur user ko sirf zaroori functionality dikhana.

# SIMPLE REAL-WORLD EXAMPLE TO UNDERSTAND ABSTRACTION:

# Example kay toor pr hum car drive karte ho.

# Hum:

# Start button
# Brake
# Accelerator
# Steering

# use karte hain.

# Lekin hamay ye nahi pata hona chahiye ke engine ke andar exactly fuel injection, combustion, sensors etc. kaise kaam kar rahe hain.

# Hamay interface milta hai, internal complexity hide hoti hai.

# Yehi abstraction hai.

# IMPORTANT:
# Python mein Abstraction Kaise Kaam Karta Hai?
# Python mein abstraction achieve karne ke liye hum ABC (Abstract Base Classes) module ka use karte hain. Isme do main concepts hote hain:

# 1) Abstract Class: Yeh ek aisi class hoti hai jiska aap direct object (instance) nahi bana sakte. Yeh sirf ek template ya framework ka kaam karti hai.

# 2) @abstractmethod: Yeh ek aisa method hota hai jiske paas sirf declaration hoti hai (koi body/logic nahi hota). Isko override karna har child class ke liye compulsory (laazmi) hota hai.


# EXAMPLE:

# class AIModel:

#     def generate(self, prompt):
#         print("Generating Response...")


# model = AIModel()

# model.generate("Hello")


# EXPLANATION:


# Hum sirf ye use kar rahe hai:

# model.generate("Hello")

# Hamay generate() ke andar kya ho raha hai, uski detail handle nahi karni:

# JASAY:

# def generate(self, prompt):
#     # API call
#     # authentication
#     # request send
#     # server processing
#     # response receive
#     # response process

# Ye internal complexity hai.

# Hamay sirf:

# model.generate("Hello")

# pata hona chahiye.

# Ye abstraction ka basic idea hai.


# EXAMPLE:

# ABC OR @abstractionmethod

# Ye abstraction ko rule dene ke liye use hote hain.

# Hum keh rahe hai:

# "Meri har AI model class mein generate() method zaroor hona chahiye."

# JASAY:


# from abc import ABC, abstractionmethod

# class AIModel(ABC):

#     @abstractionmethod
#     def generate(self, prompt):
#         pass


# Yahan:

# ABC → AIModel ko ek base/template class banata hai.

# @abstractmethod → rule banata hai:

# Jo bhi AIModel se inherit karega, usko generate() banana hi padega.


# EXAMPLE:

# class GeminiModel(AIModel):

#     def generate(self, prompt):
#         print("Gemini Response")


# class GPTModel(AIModel):

#     def generate(self, prompt):
#         print("GPT Response")

# Dono models ka generate() hai, lekin dono apne tareeqe se kaam kar rahe hain.


# Bas ye 3 cheezen yaad rakho:

# Abstraction:
# → Complex internal implementation ko hide karna.

# ABC:
# → Base/template class banana.

# @abstractmethod:
# → Child classes ke liye mandatory method ka rule lagana.


# REAL AI EXAMPLE:

# from abc import ABC, abstractmethod


# class AIModel(ABC):

#     @abstractmethod
#     def generate(self, prompt):
#         pass


# class GeminiModel(AIModel):

#       def generate(self, prompt):
#            print("Generating response using Gemini")


# model = GeminiModel()

# model.generate("Explain Python")


# Ab 4 Pillars Complete 🎯

# Pillar	      Main Idea
# Inheritance	Parent ki functionality reuse karna
# Polymorphism	Same method, different behavior
# Encapsulation	Data ko control/protect karna
# Abstraction	Complexity hide karke essential functionality expose karna


# Ek line mein 4 pillars:

# Inheritance → Reuse
# Polymorphism → Different behavior
# Encapsulation → Controlled data
# Abstraction → Hide complexity


                                          # <----------DATACLASS---------->

# - DATACLASS--->

# INTERVIEW DEFINATION:

# A dataclass is a Python class designed to mainly store data while automatically generating common methods such as __init__():

# SIMPLE UNDERSTAND:

# Python OOP may DataClass ek aisa feature hai jo hamaray code ko chota aur aasan banane ke liye use hota hai:

# MORE UNDERSTANDING:

# Normal Python class may jab hamay data store karna hota hai, toh hamay __init__, __repr__, aur __eq__ jaise boilerplate (bar bar likhne wale) methods khud likhne parte hain. DataClass in sab cheezon ko auto-generate (khud b khud create) kar deta hai, jis se hamay bohot saara time aur code bach jata hai.

# Normal Tareeqa (Without DataClass)

# class Student:

#     def __init__(self, name, age, course):
#         self.name   = name
#         self.age    = age
#         self.course = course


# student = Student("Tayyab", 18, "Python")

# print(student.name)
# print(student.age)
# print(student.course)


# YAHA HUM MANUALLY:

# self.name = name
# self.age = age
# self.course = course


# likh rahe hain.

# Agar class mein bohat saare data fields hon, to ye code baar baar likhna padta hai.


# WITH DATACLASS:(SIMPLE AND EASY)
# EXAMPLE:

# from dataclasses import dataclass


# @dataclass 
# class Student:
#     name: str
#     roll_num: int
#     grade: str


# s1 = Student("Ahmad", 18, "A+")
# print(s1)


# EXPLANATION:
# YAHA:

# from dataclasses import dataclass

# dataclass Python ki built-in functionality hai.

# OR:

# @dataclass

# Ye decorator hai jo Python ko batata hai:
# Is class ko dataclass ke rules ke according handle karo.

# Dataclass ka main benefit:

# Data-holding classes ka boilerplate code kam karna.

# Yani jo code baar baar manually likhna padta hai, dataclass usko automatically handle kar deti hai.


# 🤖 REAL AI EXAMPLE:

# Suppose hum kisi document ke chunks ka data store karna chahte hain:

# from dataclasses import dataclass

# @dataclass
# class DocumentChunk:

#     text: str
#     page_numbber: int
#     source: str


# chunk = DocumentChunk(
#     "Python is used in AI",
#     29,
#     "python_notes.pdf"
# )

# print(chunk)


# Yahan DocumentChunk mainly data store kar rahi hai:
# RAG systems mein documents/chunks ke metadata ko represent karne ke liye is type ki data structure useful ho sakti hai.


                                       # <----------PROPERTY---------->

# - @property--->

# INTERVIEW DEFINATION:
# A property allows a method to be accessed like an attribute while giving control over how its value is read or modified:

# SIMPLE UNDERSTAND:
# Python OOP mein @property ek aesa built-in decorator hai jo kisi method ko attribute (variable) ki tarah access karne ki sahulat deta hai.lekin us value ko read ya modify karne ka control method ke paas hota hai. Iski madad se hum bina brackets () lagaye kisi function ko call kar sakte hain:

# NORMAL METHPOD:
# EXAMPLE:

# class Student:

#     def __init__(self, name):
#       self.name = name

#     def get_name(self):
#        return self.name


# student = Student("Tayyab")

# print(student.get_name())

# EXPLANATION:
# YAHA
# student.get_name()

# get_name method hai, isliye () lagaye.


# AB @property:
# EXAMPLE:

# class Student:

#     def __init__(self, name):
#       self.name = name

#     @property
#     def get_name(self):
#        return self.name


# student = Student("Tayyab")

# print(student.get_name)

# EXPLANATION:
# YAHA
# print(student.get_name)
# () nahi hain.

# Lekin get_name asal mein method hi hai.
# @property ne us method ko attribute ki tarah access karne diya.


# Encapsulation se relation

# @property ko Encapsulation ke saath bohat use kiya jata hai.

# Instead of simply allowing:

# object.value

# hum decide kar sakte hain:

# value kaise read hogi
# value kaise change hogi
# value valid hai ya nahi


# @property ka actual faida kya hai?

# Main benefit hai:
# Data ko access karte waqt uske peeche logic/validation laga sakte hai, lekin bahar se woh normal attribute jaisa dikhta hai.

# @score.setter ka use tab hota hai jab hum score ki value set/change karte waqt extra logic ya validation lagana chahte hain.

# REAL AI EXAMPLE:
# Suppose RAG system mein retrieved documents ka similarity score hai:

# class SearchResult:

#     def __init__(self, score):
#         self._score = score

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):

#         if 0 <= value <= 1:
#             self._score = value

#         else:
#             print("Score must be between 0 and 1")


# result = SearchResult(0.88)

# print(result.score)

# result.score = 0.93

# print(result.score)


# ONE-LINE LEARN:
# @property = Method ko attribute ki tarah access karna + value par control rakhna.