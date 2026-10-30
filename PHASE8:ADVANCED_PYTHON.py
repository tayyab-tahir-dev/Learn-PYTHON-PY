                                # <----------PHASE 8: ADVANCED_PYTHON---------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1)List Comprehension
# 2)Dict Comprehension
# 3)Set Comprehension
# 4)Generators
# 5)Iterators
# 6)Context Managers
# 7)Decorators
# 8)Type Hints
# 9)Protocol
# 10)ABC
# 11)Enums
# 12)NamedTuple
# 13)Dataclass
# 14)Slots



                                        # <----------LIST COMPREHENSION---------->

# - 1) List Comprehension--->

# INTERVIEW DEFINATION:
# List comprehension is a concise way to create a new list by applying an expression to items from an iterable, optionally filtering those items with a condition.

# SIMPLE UNDERSTAND:
# List comprehension Python mein nayi list banane ka short aur readable tareeqa hai, jisme hum existing items par operation kar sakte hain aur condition laga kar kuch items select kar sakte hain.


# BASIC SYNTAX:

# new-list = [expression for item in iterable]

# Har part ka matlab:
# - new_list: Nayi list jisme results store honge.
# - []: Square brackets — list banane ke liye.
# - expression: Har item par kya operation karna hai.
# - for: Items ko ek ek karke process karta hai.
# - item: Current item ka temporary variable.
# - in: Batata hai ke items kis collection se lene hain.
# - iterable: Aisi cheez jiske items ek ek karke access kiye ja sakte hain, jaise list ya tuple.


# 1) BASIC EXAMPLE:

# numbers = [1, 2, 3, 4, 5,]

# square = [number **2 for number in numbers]

# print(square)



# - number ** 2 har number ka square nikalta hai.
# - for number in numbers numbers ko ek ek karke leta hai.
# - squares mein results ki nayi list banti hai.



# Condition ke saath List Comprehension
# SYNTAX:

# new_list = [expression for item in iterable if condition]


# 2) BASIC EXAMPLE:

# numbers = [1, 2, 3, 4, 5, 6]

# even_numbers = [
#     number for number in numbers
#     if number % 2 == 0
# ]

# print(even_numbers)


# Yahan:
# - % remainder nikalta hai.
# - number % 2 == 0 check karta hai ke number 2 se divide hone par remainder zero hai ya nahi.
# - if condition false hone par us number ko nayi list mein include nahi kiya jata.


# 3) AI EXAMPLE:
# Maan lo hamare paas documents ke text chunks hain aur hum empty chunks ko remove karna chahte hai.


# chunks = [    
#     "Python is useful for AI.     ",
#     "",
#     "      Embeddings represent text as vectors.",
#     "   ",
#     "RAG retrieves relevant documents."
# ]

# clean_chunks = [
#     chunk.strip()
#     for chunk in chunks
#     if chunk.strip()
# ]

# print(clean_chunks)



# strip() text ke start aur end se whitespace remove karta hai.
# if chunk.strip() empty ya whitespace-only text ko reject karta hai.
# clean_chunks mein cleaned, non-empty text store hota hai.



                                        # <----------DICTIONARY  COMPREHENSION---------->

# 2) - Dictionary Comprehension--->

# INTERVIEW DEFINATION:
# Dictionary comprehension is a concise way to create a dictionary by generating key-value pairs from an iterable, optionally applying a condition.

# SIMPLE UNDERSTAND:
# Dictionary comprehension Python mein ek short tareeqa hai jisse hum key:value pairs ki madad se nayi dictionary bana sakte hain, aur zaroorat par condition bhi laga sakte hain.


# BASIC SYNTAX:

# new_dict = {key: value for item in iterable}



# {} — dictionary banane ke liye.
# key — dictionary mein unique identifier.
# : — key aur value ko separate karta hai.
# value — key ke saath store hone wala data.
# for — items ko ek ek karke process karta hai.
# item — current item.
# iterable — jaise list ya tuple, jiske items process honge.


# BASIC EXAMPLE:
# numbers ke squares

# numbers = [1, 2, 3, 4, 5, 6]

# squares = {
#     number: number ** 2
#     for number in numbers
# }

# print(squares)



# BASIC EXAMPLE:
# Conditon ke saath
# Sirf even numbers ki dictionary banaana:

# numbers = [1, 2, 3, 4, 5, 6]

# even_square = {
#     number: number ** 2
#     for number in numbers
#     if number % 2 == 0
# }

# print(even_square)



# AI EXAMPLE:
# Maan lo hamari AI document-processing project mein har document ka naam aur uske text ki length record karni hai.

# documents = {
#     "python.txt": "Python is useful for AI",
#     "rag.txt": "RAG retrieves relevant documents",
#     "ai.txt": "AI processes information"
# }

# document_length = {
#     name: len(text)
#     for name, text in documents.items()
# }

# print(document_length)


# Is example mein:
# - .items() dictionary ke key-value pairs deta hai.
# - name mein document ka naam aata hai.
# - text mein uska content aata hai.
# - len(text) characters ki tadaad count karta hai.

# Ye document metadata aur text-processing pipelines mein useful ho sakta hai.



                                          # <----------SET COMPREHENSION---------->

# 3) - Set Comprehension--->

# INTERVIEW DEFINATION:
# Set comprehension is a concise way to create a set from an iterable using an expression and an optional condition.

# SIMPLE UNDERSTAND:
# Set comprehension ek short tareeqa hai jis se hum kisi iterable se expression aur optional condition use karke naya set banate hain.


# BASIC EXAMPLE:

# numbers = [1, 2, 2, 3, 3, 4, 5, 5]

# unique_numbers = {
#     number
#     for number in  numbers
# }

# print(unique_numbers)



# Yahan kya hua?

# - numbers list mein 2 aur 3 do-do baar hain.
# - for number in numbers har number ko leta hai.
# - Set duplicate values ko sirf ek baar rakhta hai.
# - Is liye result mein har number ek hi baar hai.

# IMPORTANT: Set ki values unique hoti hain, aur unka output order zaroori nahi ke list jaisa ho.


# BASIC EXAMPLE:
# Condition ke saath
# Sirf even numbers ka set:

# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]

# unique_even_numbers = {
#     number 
#     for number in numbers
#     if number % 2 == 0
# }

# print(unique_even_numbers)



                                         # <----------GENERATORS---------->

# 4) - Generator--->

# INTERVIEW DEFINATION:
# A generator is a special type of iterator that produces values one at a time, only when requested.

# SIMPLE UNDERSTAND:
# Generator Python ka ek special mechanism hai jo values ko ek-ek karke tab produce karta hai jab unki zaroorat hoti hai, bajaye iske ke saari values ek saath bana le.


# BASIC EXAMPLE:

# def generate_numbers():
#     yield 1
#     yield 2
#     yield "How are you"

# numbers = generate_numbers()

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


# Har keyword ka matlab

# - def — function banata hai.
# - generate_numbers — function ka naam hai.
# - yield — ek value produce karta hai aur function ki current state ko temporarily save kar deta hai.
# - numbers — generator object ko store karta hai.
# - next() — generator se agli value nikalta hai.

# Important: Normal function mein return value de kar function ko khatam kar deta hai. Generator mein yield value deta hai aur function ko pause kar deta hai; agli next() call par woh wahin se continue karta hai.



# (Why use it?)

# 1. Memory Bachati Hai (Memory Efficient):
# Agar aapko 1 Lakh numbers par kaam karna hai, toh normal function 1 Lakh numbers ki list banakar memory (RAM) bhar dega. yield ek waqt mai sirf ek number generate karta hai, isliye memory bohot kam istemal hoti hai.

# 2. Time Bachata Hai:
# Aapko saara data tayyar hone ka intezar nahi karna parta, pehli value aate hi aap uspar kaam shuru kar sakte hain


# AI EXAMPLE:

# def read_documents():
#     yield "Python document" 
#     yield "RAG document"
#     yield "AI document"

# for document in read_documents():
#     print(document)



                                            # <----------ITERATORS---------->

# 5) - iterators--->

# INTERVIEW DEFINATION:
# An iterator is an object that returns one item at a time when requested and remembers its current position.

# SIMPLE UNDERSTAND:
# Iterator aisa object hai jo request karne par ek waqt mein ek item deta hai aur apni current position yaad rakhta hai.


# BASIC EXAMPLE:

# Yeh ek normal list hai (Iterable)
# meri_list = ["Amna", "Ali", "Zain"]

# # Isko iterator banate hain
# mera_iterator = iter(meri_list)

# # Ab ek ek karke items nikalte hain
# print(next(mera_iterator))  # Output: Amna
# print(next(mera_iterator))  # Output: Ali
# print(next(mera_iterator))  # Output: Zain

# Agar aap dobara next() chalayein ge toh error aayega: StopIteration


# Important: List khud iterable hai, jabke iter(numbers) se milne wala object iterator hai.


# - Iterable: Aisi cheez jiske items par loop chala sakte hain, jaise list, tuple aur string.
# - Iterator: Aisa object jo next() se ek-ek item deta hai.


# IMPORTANT:
# Aghar iterator khatam ho jaye to?

# Teesri next() call par StopIteration error aayega, kyun ke list ke dono items pehle hi mil chuke hain.



# Generators aur Iterators mein difference:

# Generator	                                    Iterator

# Values produce karne ka ek tareeqa hai.       	Values ko ek-ek karke access karne wala object hai.
# Aksar yield se banta hai.	                    iter() ya custom iterator class se mil sakta hai.
# Generator khud iterator hota hai.	            Har iterator generator nahi hota.



                                       # <----------CONTEXT MANAGES---------->

# 6) - Context Manager--->

# INTERVIEW DEFINATION:
# A context manager is an object that manages the setup and cleanup of a resource, typically using Python's with statement.

# SIMPLE UNDERSTAND:
# Context manager aisa mechanism hai jo kisi resource ko use karne se pehle setup aur kaam khatam hone par cleanup manage karta hai.