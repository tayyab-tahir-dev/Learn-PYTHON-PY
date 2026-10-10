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

# 2) - TXT-->

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


# - readline() or readlines()--->

# - readline()-->
# Yeh aik file methods hai jo file se ek waqt mein ek line read karta hai.

# EXAMPLE:

# with open("learn.txt", "r") as file:
#     line = file.readline()
#     print(line)


# YEH AIK TIME MAI AIK LINE READ KRTA HAI:

# AGHAR DUSRI LINE BI READ KRNI HO:

# with open("learn.txt", "r") as file:
#     first_line  = file.readline()
#     second_line = file.readline()

# print(first_line)
# print(second_line)

# Important:
# Har readline() call file mein agali line ki taraf move karti hai. Naya file open karne par reading position shuru se hoti hai.


# - readlines()--->

# readlines() file ki tamam remaining lines read karke list mein return karta hai.

# EXAMPLE:

# with open("learn.txt", "r") as file:
#     lines = file.readlines()

# print(lines)


# IMPORTANT:
# YEH LIST RETURN KARAY GA:kyun ke ye file ki har line ko list ke alag element mein store karta hai.



                                            # <----------CSV---------->

# 3) - CSV--->

# INTERVIEW DEFINATION:
# CSV (Comma-Separated Values) is a file format used to store tabular data in rows and columns.

# SIMPLE UNDERSTAND:
# CSV aik file format hai jisme data rows aur columns ki form mein store hota hai, aur aam tor par values commas , se separate hoti hain.

# Row: Data ki aik horizontal line. LEFT TO RIGHT:
# Column: Aik category, jaise Name, Age ya Course.
# Comma ,: Values ko separate karta hai.

# EXAMPLE:

# SUPPOSE YEH AIK TABLE HAI:

# students.csv

# Name	    Age 	Course
# Tayyab	18	    Python
# Ali	    20	    AI
# Ahmed	    19	    Data Science

# YEH studnet.csv FILE MAI IS TARAH STORE KIYA JAYE GA:

# Name,Age,Course
# Tayyab,18,Python
# Ali,20,AI
# Ahmed,19,Data Science


# CSV kyun use hoti hai?
# CSV tab useful hoti hai jab data records ki form mein ho.
# - Students ka record
# - Customers ka data
# - AI training datasets
# - Product lists


# Important: 
# CSV file ka data text-based hota hai. Python se read karne par numbers bhi aam tor par strings ki form mein milte hain; zaroorat par unhein int ya float mein convert karna hota hai.



# - csv MODULE--->

