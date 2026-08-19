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
# Aakhir mein CPU task perform karta hai or result show krvata hai.

# CPU khud screen par result show nahi karta. CPU calculation/operations karta hai, phir 
# operating system + terminal/display system result ko screen par show karte hain.



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


