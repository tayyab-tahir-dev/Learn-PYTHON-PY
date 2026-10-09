                                # <----------PHASE 6: FILES---------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1) Files
# 2) txt
# 3) csv
# 4) json
# 5) pathlib
# 6) Real AI project examples



                                         # <----------FILES---------->

# 1) - Files--->

# INTERVIEW DEFINATION:
# A file is a named location on a computer used to permanently store data so that it can be accessed and used later.

# SIMPLE UNDERSTAND:
# File computer mein data ko save karke rakhne ki jagah hoti hai.


# Variable:
# Temporary data during program execution.
# File:
# Data ko permanently store karne ke liye.

# Examples:
# .txt
# .csv
# .json
# .pdf
# .jpg

# AI Use:
# Documents, datasets, API data, configurations
# aur knowledge-base data ko store/read karna.


                                        # <----------TXT---------->

# - TXT-->

# Definition:
# A TXT file is a plain-text file used to store readable text data.

# SIMPLE UNDERSTAND:
# TXT file aik simple file hoti hai jisme hum normal text/data store karte hain.


# SIMPLE Example:

# knowledge.txt

# File kay Andar:

# Python is a programming language.
# AI uses Python for many applications.


# Python mein TXT file ke saath kya kar sakte hain?
# Basic level par 3 important kaam:

# Read    → file se data lena
# Write   → file mein data likhna
# Append  → existing data ke end mein new data add karna

# In kaam ke liye Python mein sabse important function:

# open()


# - open--->

# INTERVIEW DEFINATION: 
# open() is a built-in Python function used to open a file for reading, writing, or other file operations.

# SIMPLE UNDERSTAND:
# open() Python ko batata hai ke kis file ko access karna hai aur kis purpose ke liye.

# BASIC SYNTAX:
# open("filename", "mode")

# BASIC EXAMPLE:
# file = open("learn.txt", "r")

# YAHAN:

# "learn.txt"   → file ka naam
# "r"           → read mode
# file          → opened file ko refer karne wala variable


#  - "r"--> READ

# r ka mtlb "READ MODE" hota hai,
# yeh  python ko btata hai kay tumhara maqsad file se data read karna hai, na ke file ke data ko modify ya write karna.

# EXAMPLE:

# file = open("learn.txt", "r")

# content = file.read()

# print(content)

# file.close()


# - with open()-->

# with open() Python mein file ko safely open aur automatically close karne ka recommended tareeqa hai.

# with open() file ko open karta hai aur jab uska kaam complete ho jata hai to automatically file close kar deta hai.

# EXAMPLE:

# with open("learn.txt", "r") as file:
#     documents = file.read()

# print(documents)


# - "w"---> WRITE

# "w" mode file mein data likhne ke liye use hota hai. Agar file exist nahi karti to Python use create kar deta hai. Agar file pehle se exist karti hai, to uska purana content replace ho jata hai.

# EXAMPLE:

# with open("learn.txt", "w") as file:
#      file.write("LEARNING PYTHON:\n")
#      file.write("PYTHON FOR AI ENGINEERING")


# IMPORTAND:
# \n ka mtlb new line:


# - "a"---> APPEND

# a mode file ke last mein naya data add karta hai or purana data preserve/save rakhta hai.

# EXAMPLE:

# with open("learn.txt", "a") as file:
#     file.write("\nPYTHON IS GOOD FOR AI")