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


# - open---> (PART-1)

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


#  - "r"--> READ (PART-2)

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


# - "w"---> WRITE (PART-3)

# "w" mode file mein data likhne ke liye use hota hai. Agar file exist nahi karti to Python use create kar deta hai. Agar file pehle se exist karti hai, to uska purana content replace ho jata hai.

# EXAMPLE:

# with open("learn.txt", "w") as file:
#      file.write("LEARNING PYTHON:\n")
#      file.write("PYTHON FOR AI ENGINEERING")


# IMPORTAND:
# \n ka mtlb new line:


# - "a"---> APPEND (PART-4)

# a mode file ke last mein naya data add karta hai or purana data preserve/save rakhta hai.

# EXAMPLE:

# with open("learn.txt", "a") as file:
#     file.write("\nPYTHON IS GOOD FOR AI")


# - readline() or readlines()---> (PART-6)

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


# - readlines()---> (PART-5)

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



# - csv MODULE---> (PART-1)

# INTERVIEW DEFINATION:
# The csv module is a built-in Python module used to read and write CSV files.

# SIMPLE UNDERSTAND:
# csv module Python ka built-in module hai jo CSV files ka data read aur write karne ke liye use hota hai.

# EXAMPLE:

# import csv

# with open("learn.csv",  "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# OUTPUT:

# ['Name', 'Age', 'Course']
# ['Tayyab', '18', 'Python']
# ['Ali', '20', 'AI']
# ['Ahmed', '19', 'Data Science']


# EXPLANATION:

# import csv         — CSV module ko program mein use karne ke liye import karta hai.

# newline="",        — CSV file read karte waqt newline handling ko theek

# encoding="utf-8"   — text ko sahi tareeqe se read karne mein madad karta hai

# csv.reader(file)   — file ka CSV data read karta hai.
# for row in reader  — har row ko ek ek karke access karta hai.
# print(row)         — har row ko print karta hai.
# row                — har row ki values ki list hoti hain.



# encoding="utf-8" = Unicode Transformation Format - 8-bit.

# Important: 
# CSV se read hone wali values strings hoti hain. Misal ke taur par "18" string hai, integer 18 nahi.

# SAVE(encode)
# READ(decode)



# - csv writter()---> (PART-2)
# csv.writer() CSV file mein data ko rows ki form mein likhne ke liye use hota hai.


# EXAMPLE:

# import csv

# with open("learn.csv", "w", newline="", encoding="utf-8") as file:
#     write = csv.writer(file)

#     write.writerow(["Name", "Age", "Course"])
#     write.writerow(["Tayyab", "18", "Python"])
#     write.writerow(["Ali", "24", "JavaScript"])


# writer.writerow([...]) — CSV file mein ek row likhta hai.



                                           # <----------JSON---------->

# - json--->

# INTERVIEW DEFINATION: 
# JSON (JavaScript Object Notation) is a text-based data format used to store and exchange structured data.

# SIMPLE UNDERSTAND:
# JSON aik text-based format hai jo structured data ko store aur applications ke darmiyan exchange karne ke liye use hota hai.

# IMPORTANT:
# Jab hamari Python application kisi AI API ko request bhejti hai, to data aksar JSON format mein bheja jata hai.

# EXAMPLE:

# {
#     "app_name": "AI Assistant",
#     "model": "GPT",
#     "temperature": 0.7,
#     "max_tokens": 500,
#     "debug": True
# }



# DIFFERENCE:
# JSON AND PYTHON DICTIONARY:
# Dono similar dikhte hain, lekin kuch differences hain:

# Python Dictionary	                     JSON
# Python ke andar data structure hai:	 Data store/exchange karne ka format hai
# Boolean True hota hai	                 Boolean true hota hai:
# Python mein use hoti hai	             Files aur APIs mein use hota hai:


# JSON mein true, false, null use hote hain; Python mein True, False, None.



# - JSON MODULE---> (PART-1)
# JSON Python ka built-in module hai jo Python ke data ko JSON format STRINGS mein aur JSON data ko Python objects mein convert karta hai. 

# JSON Python ka built-in module hai, aur dump(), dumps(), load(), loads() is module ke functions hain.

# dumps()   AND   loads()

# 1) dumps()
# Python dictionary ko JSON formate ki string mai convert krta hai:
# EXAMPLE:

# import json

# # A Python dictionary
# learn_json = {
#     "name": "Alice",
#     "is_admin": True,
#     "roles": ["developer", "manager"],
#     "budget": None
# }

# # Convert Python dict to JSON string
# json_string = json.dumps(learn_json)

# print(json_string)


# 2) loads()
#  JSON String ko Python Object mai convert krta hai:
# EXAMPLE:

# import json

# learning_json = '{"name": "Alice", "is_admin": true, "roles": ["developer", "manager"], "budget": null}'

# python_dict = json.loads(learning_json)

# print(python_dict)