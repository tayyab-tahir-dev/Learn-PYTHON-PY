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