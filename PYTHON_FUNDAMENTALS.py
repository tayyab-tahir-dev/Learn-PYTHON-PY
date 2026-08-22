# What is PYTHON?
# PYTHON is a high-level programming language used to give instructions to computers and build 
# different types of applications, and softwares etc.  


# What is REPL?
# REPL stands for Read, Eval, Print, Loop. It is an interactive programming environment that
# takes single user inputs (i.e. single expressions), evaluates them, and returns the result to 
# the user. The REPL environment is a great way to test out code snippets and see immediate 
# results.

# SIMPLE EXAMPLE OF REPL IS:
# REPL mai hum apna code line-by-line likhte hai aur uska output immediately dekhta hai.For 
# testing



                   # <--------INTERPRETER IN PYTHON----------->


# A Python interpreter is a program that reads and executes Python code so your computer can run 
# it.

# Hum PYTHON code likhtay hai 

# print("Hello World")

# Python code ko read krti hai
# code ko bytecode mein convert karti hai.
# Python Virtual Machine (PVM) us bytecode ko execute karti hai.
# Aakhir mein CPU task perform karta hai 
# operating system + terminal result show krvata hai.

# CPU khud screen par result show nahi karta. CPU calculation/operations karta hai, phir 
# /display system result ko screen par show karte hain.



                    # <--------NAMING RULE IN PYTHON----------->



# NAMING RULE mtlb ki hum variable ka naam kaise rakh sakte hai.Inkay kuch rules hai jo hume 
# follow karnay parta hai.

# EXAMPLE 

# 1) Naam letter ya underscore say start hona chahiye.
# 2) Naam may letter,numbers or underscore use kr sktay hai.
# 3) Naam may space use nhi kr sktay.


                      #  <------------VARIABLES---------------->


# Python variables are used to store/refer data (objects) so we can use that data later in a program.

# Python mein variable ek naam hota hai jo kisi object ya value ko refer karta hai. Python mein 
# variable banane ke liye var, let ya const jaisa koi keyword use nahi hota, hum simply 
# name = value likhte hain.

# PYTHON mai JS ki tarah variable declare karne ke liye 'var','let' ya 'const' ka use nhi karte.

# print() function console.log() ki tarah kaam karta hai.

# How to create a variable in PYTHON?

# name = "Tayyab"
# print(name)

# name is the variable name.
# = mtlb assign the value in the variable.
# "Tayyab" is the value of that variable.


 
                            #  <-----------DATA TYPES-------------->


# INTERVIEW STYLE DEFINATION:
# A DATATYPE defines the type of value and determines what operations can be performed on that 
# value.

# TYPES of DATATPES in PYTHON:
# 1) Numeric Data Types:
#     a) Integer               
#     b) Float                 
#     c) Complex               
# 2) Sequence Data Types:
#     a) String 
#     b) List
#     c) Tuple
# 3) Set Data Types:
#     a) Set
# 4) Mapping Data Types:
#     a) Dictionary

# USE OF TYPE() FUNCTION:
# A TYPE() Function is used to check DATATYPE of values.


                             # <----------DYNAMIC TYPING---------->


# INTERVIEW STYLE DEFINATION:
# DYNAMIC TYPING means that in Python, you don't need to declare the data type of a variable 
# explicitly; Python determines the type at runtime.

# Python mein variable ka data type permanently fixed nahi hota. Jo value variable ko di jati 
# hai, Python runtime par us value ka type determine karta hai.Hum baar baar variable ki value 
# change kr sktay hai or uska DATATYPE bi change ho jata hai.Isko DYNAMIC TYPING kehtay hai.

# EXAMPLE:

# Yha pr aik he variable hai 'a' but uski value or datatype change ho rhi hai.

# a = 10
# print(a)
# print(type(a))

# a = "Tayyab"
# print(a)
# print(type(a))

# a = True
# print(a)
# print(type(a))



                # <----------------MEMORY IN PYTHON----------------->



# INTERVIEW STYLE DEFINATION:
# Memory (RAM) is the part of a computer where data and objects are temporarily stored while a 
# program is running.

# Memory (RAM) computer ki woh jagah hai jahan program ke run hone ke waqt data aur objects 
# temporarily store hote hain.                

# Python program run hota hai to Python ko apne objects ke liye computer ki memory use karni 
# parti hai.

# EXAMPLE:

# x = 10
# Is code ko run karne par Python 10 ko memory mein ek object ke taur par rakhta hai.or x us object
# ko reffer krta hai.

# print(x)
# Or jub hum yha x ki value print kartay hai to python memory may ja ke x ka refference find krta 
# hai or us object ki value ko print krta hai.



                      # <---------------REFERENCE IN PYTHON--------------->


# INTERVIEW STYLE DEFINATION:
# A REFERENCE is a connection between a variable name and an object in memory, allowing the 
# variable to access that object.

# Reference variable name aur object ke darmiyan connection hota hai, jiski wajah se name us 
# object ko access kar sakta hai.

# Jab hum variable ko kisi value say assign karte hain, Python us value ke liye memory mein ek 
# object create karta hai aur variable name ko us object ka reference assign karta hai. 

# Multiple names can reffer to same object.

# x = 10

# Python 10 ka object memory mein create karta hai.
# 10 wala object memory mein exist karta hai.
# Python x naam ko us 10 object ke saath associate karta hai.
# Ab x 10 ko refer karta hai

# Jub Hum.

# print(x)

# likhtay hai, Python x ke through 10 object ko access karta hai aur 10 result milta hai.



                     # <--------BYTECODE IN PYTHON----------->


#  BYTECODE is an intermediate form of our code that is executed by the Python Virtual Machine 
# (PVM).

# BYTECODE mein conceptually instructions hoti hain:

# 10 ko load karo
# x mein store karo
# x ki value lao
# print karo

# PHIR KAAM (PVM) KARTA HAI:
# Phir PVM in bytecode instructions ko one by one execute karti hai.


 
                    # <--------PYTHON VIRTUAL MACHINE (PVM)----------->


# PVM (Python Virtual Machine) Python ke andar ek execution engine hoti hai jo bytecode ko 
# execute karti hai.
# Yani PVM ka main kaam hai:
# Bytecode ki instructions ko read karna aur unko execute karna.



                # <--------------MUTABLE VS IMMUTABLE----------->


# MUTABLE:
# INTERVIEW STYLE DEFINATION: 
# Mutability is the ability of an object to be modified after it has been created.

# Mutability ka matlab hai: kisi existing object ko create hone ke baad modify kar sakna.

# EXAMPLE OF MUTABLE OBJECTS:
# List, Set, Dictionary


# IMMUTABLE:
# INTERVIEW STYLE DEFINATION:
# Immutability means that an object cannot be modified after it has been created.

# Immutability ka matlab hai: kisi existing object ko create hone ke baad uski value modify nahi 
# kar sakte.Balkay new object create kr kay refer kr sktay hai.

# EXAMPLE OF IMMUTABLE OBJECTS:
# String, Tuple, Integer, Float, Boolean



               # <-----------------OPERATORS----------------->


# INTERVIEW STYLE DEFINATION:

# An OPERATOR is a symbol or keyword used to perform an operation on values or objects.

# SIMPLE  UNDERSTANDING:
# OPERATOR ek special symbol ya keyword hota hai jo Python mein values/objects par koi operation 
# perform karne ke liye use hota hai.


# TYPES OF OPERATORS:

#1) Arithmetic Operators
#2) Comparison Operators
#3) Assignment Operators
#4) Logical Operators
#5) Identity Operators
#6) Membership Operators


#1) Arithmetic Operators:
# INTERVIEW STYLE DEFINATION:

# Arithmetic Operators are used to perform mathematical operations like addition, subtraction,
# multiplication, division, etc. on numeric values.

# TYPES OF ARITHMETIC OPERATORS:
# 1) Addition (+)

# a = 10
# b = 5
# print(a + b) # Output: 15


# 2) Subtraction (-)

# print(a - b) # Output: 5


# 3) Multiplication (*)

# print(a * b) # Output: 50


# 4) Division (/)

# print(a / b) # Output: 2.0


# 5) Floor Division (//)

# print(a // b) # Output: 2


# 6) Modulus (%)

# print(a % b) # Output: 0


# 7) Exponentiation (**)

# print(a ** b) # Output: 100000



# 2) Comparison Operators:
# INTERVIEW STYLE DEFINATION:

# Comparison Operators are used to compare two values and return a Boolean result (True or False).

# SIMPLE UNDERSTANDING:
# Comparison operators ka kaam do values ko compare karna hota hai.

# TYPES OF COMPARISON OPERATORS:

# 1) Equal to (==)

# a = 10
# b = 5
# print(a == b) # Output: False


# 2) Not equal to (!=)

# print(a != b) # Output: True


# 3) Greater than (>)

# print(a > b) # Output: True


# 4) Less than (<)

# print(a < b) # Output: False


# 5) Greater than or equal to (>=)

# print(a >= b) # Output: True


# 6) Less than or equal to (<=)

# print(a <= b) # Output: False



# 3) Assignment Operators:
# INTERVIEW STYLE DEFINATION:

# Assignment Operators are used to assign values to variables.

# SIMPLE UNDERSTANDING:
# Assignment operators ka kaam variable ko value assign karna hota hai.

# TYPES OF ASSIGNMENT OPERATORS:

# 1) Assignment (=)
# a = 10

# 2) Add and assign (+=)

# a = 10
# a += 5 
# print(a) # Output: 15


# 3) Subtract and assign (-=)

# a = 10
# a -= 5
# print(a) # Output: 5


# 4) Multiply and assign (*=)

# a = 10
# a *= 5
# print(a) # Output: 50


# 5) Divide and assign (/=)

# a = 10
# a /= 5
# print(a) # Output: 2.0


# 6) Floor divide and assign (//=)

# a = 10
# a //= 5
# print(a) # Output: 2


# 7) Modulus and assign (%=)

# a = 10
# a %= 5
# print(a) # Output: 0


# 8) Exponentiate and assign (**=)

# a = 10
# a **= 5
# print(a) # Output: 100000


# 4) LOGICAL OPERATORS:
# INERVIEW STYLE DEFINATION:

# Logical operators are used to combine or manipulate Boolean conditions.

# SIMPLE UNDERSTANDING:

# Logical operators Boolean conditions ko combine ya reverse karne ke liye use hote hain.

# TYPES OF LOGICAL OPERATORS:
# 1) LOGICAL AND
# 2) LOGICAL OR
# 3) LOGICAL NOT 

# 1) LOGICAL AND:
# TUB TRUE DETA HAI JUB DONO CONDITONS TRUE HO.

# a = 10
# b = 20
# print(a > 5 and b < 30)


# 2) LOGICAL OR:
# TUB TRUE DETA HAI JUB KAM AZ KAM 1 CONDITION TRUE HO:

# a = 10
# b = 20
# print(a > 5 or b < 10)


# 3) LOGICAL NOT:
# RESULT KO REVERSE (TRUE KO FALSE OR FALSE KO TRUE) KR DETA HAI:

# a = 10
# print(not (a > 5))



# SIMPLE:

# and → dono conditions True honi chahiye
# or  → kam az kam ek condition True honi chahiye
# not → result ko reverse karta hai


# IMPORTANT:

# True and True   → True
# True and False  → False

# True or False   → True
# False or False  → False

# not True        → False
# not False       → True

# Use kahan hota hai?

# Logical operators tab useful hote hain jab program mein ek se zyada conditions ko check karna 
# ho. 



                # <-----------IDENTITY OPERATOR----------->

# INTERVIEW STYLE DEFINATION:
# IDENTITY OPERATORS are used to check whether two variables refer to the same object.

# SIMPLE UNDERSTAND:
# IDENTITY OPERATORS check karte hain ke do variables same object ko refer kar rahe hain ya nahi.
# Memory location same hai ya nhi.

# TYPES OF IDENTITY OPERATORS:
# 1) is
# 2) is not 

# 1) is
# The operator is used to compare whether two objects are same or not.It returns TRUE when memory
# location of two are same else it returns false.

# EXAMPLE:
# a = 10
# b = 10
# print(a is b)


# 2) is not
# This operator is works in reverse manner for is operator.
# It returns true if memory location of two objects are not same and if they are same it returns 
# false.

# EXAMPLE:

# a = 10
# b = 20 
# print(a is not b)




                   # <----------MEMBERSHIP OPERATOR---------->


# INTERVIEW STYLE DEFINATION:
# Membership operators are used to check whether a value exists in a sequence or collection.

# SIMPLE UNDERSTANDING:
# Membership operators check karte hain ke koi value kisi collection ya sequence ke andar
# موجود hai ya nahi.

# TYPES OF MEMBERSHIP OPERATOR:
# 1) in
# 2) not in

# 1) in
# Check krta hai Kya ye value is collection ke andar موجود hai?

# EXAMPLE:

# numbers = [10, 20, 30]
# print(10 in numbers)


# 2) not in
# Check krta hai Kya ye value collection ke andar موجود nahi hai?

# EXAMPLE:

# numbers = [10, 20, 30]
# print(10 not in numbers)



                     # <----------STRING DATATYPE---------->


# INTERVIEW STYLE DEFINATION:
# A string is a sequence of characters used to represent text in Python.

# SIMPLE UNDERSTANDING:
# String characters ka sequence hota hai jo Python mein text represent karne ke liye use hota hai.

# Har vo chiz jo (' ') ya double (" ") quotes ke andar ho, woh string hota hai. 

# EXAMPLE:

# a = "Tayyab"
# print(type(a))


# int value hai but jub quotes may likh to yeh bi string ban gyi.

# b = "10"
# print(type(b))

# Asay he koi bi type ka data ho usko double ya single quotes may likh  do vo string ban jay gi.



                        # <----------F-STRING---------->



# INTERVIEW STYLE DEFINATION:
# An f-string is a string that allows variables and expressions to be embedded directly inside 
# it using curly braces {}.

# SIMPLE:
# f-string aisi string hoti hai jisme hum variables ya expressions ki values directly text ke 
# andar insert kar sakte hain.

# SOME EXAMPLES:

# name = "TAYYAB"
# print(f"My Name is {name}")


# my_name = "Tayyab"
# my_age = 18
# print(f"My Name Is {my_name} And I'm {my_age} Years Old")


# a = 10
# b = 20
# total = (f"Total is {a + b}")
# print(total)


# name = "Tayyab"
# age = 18

# print(f"My Name Is {name}")
# print(f"My Age Is {age}")
# print(f"Next Year I Will Be {age + 1}")




                        # <----------NUMBERS---------->
# Python mein numbers represent karne ke liye different numeric data types available hain.

# TYPES:
# 1) int
# 2) float 
# 3) complex


# 1) int

# INTERVIEW STYLE DEFINATION:
# int represents whole numbers without a decimal point.
# NEGATIVE numbers bi int hai.

# EXAMPLE:

# a = 20
# print(type(a))


# temperature = -5
# print(type(temperature))


# 2) float:
# float represents numbers with a decimal point.
# yha bi NEGATIVE NUMBERS float may atay hai.

# EXAMPLE:

# a = 5.9
# print(type(a))


# temperature = -2.3
# print(type(temperature))


# 3) COMPLEX:
# complex represents numbers with real and imaginary parts.
# Python mein j imaginary part ko represent karta hai:

# EXAMPLE:

# z = 2 + 5J
# print(type(z))