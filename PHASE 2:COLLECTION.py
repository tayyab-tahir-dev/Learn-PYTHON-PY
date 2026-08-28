                  # <----------PHASE 2: COLLECTION:---------->


# LIST

# INTERVIEW STYLE DEFINATION:
# A Python list is an ordered, mutable collection that can store multiple items, including 
# duplicates and different data types.

# SIMPLE UNDERSTANDING:
# List Python mein ek ordered aur mutable collection hai jo multiple items ko store karti hai.


# Properties:
# - Ordered
# - Mutable
# - Allows duplicates
# - Can store different data types
# - Uses [ ]
# - Supports indexing
# - Supports negative indexing

# Important: LIST ADDITION METHODS:
# len()     → checks length of list
# append()  → adds one item at the end
# insert()  → adds an item at a specific index
# extend()  → adds multiple items


# SYNTAX:
# my_list = [item1, item2, item3]


# - ORDERED--->:
# List mein elements jis order mein add kiye jaate hain, wohi order maintain rehta.
# Iska matlab hai items ek specific sequence/position mein stored hote hain.

# item1      → 0
# item2      → 1
# item3      → 2

# Python mein indexing 0 se start hoti hai.


# - MUTABLE--->:
# Object banne ke baad uske contents ko change/modify kar sakte hain.


# students = ["AHMAD", "ALI", "TAYYAB"]

# students[1] = "SUBHAN"

# print(students)


# yaha pr index [1] pr "ALI" ki jagha "SUBHAN" add kr dia.


# - ALLOW DUPLICATES--->:
# List mein same value multiple times aa sakti hai.

# numbers = [10, 20, 30, 10, 20, 30,]
# print(numbers)


# THEY CAN STORE DIFFERENT DATATYPES--->:

# data_types = ["TAYYAB", 18, 3.90, True]
# print(data_types)


# - len()--->
# LIST KI LENGTH:
# List mein kitne items hain, ye len() se check karte hai.

# length = ["LENGTH1", "LENGTH2", "LENGTH3"]
# print(len(length))

# len() returns the number of items in a list.


# - EMPTY LIST--->:
# Agar list mein koi item nahi hai.

# list = []
# print(list)


# - LIST MAY ITEMS KO ACCESS KRNA--->:
# Indexing use hoti hai.

# students = ["TAYYAB", "ALI", "AHMAD"]

# print(students[0])
# print(students[1])
# print(students[2])

# NEGATIVE INDEXING:
# Negative may indexing -1 say start hoti hai.

# students = ["TAYYAB", "ALI", "AHMAD"]

# print(students[-1])
# print(students[-2])
# print(students[-3])

# TAYYAB      → -3
# ALI         → -2
# AHMAD       → -1


# - append()--->
# List kay last may aik item add krvana.

# menu = ["FRIES", "BURGER"]

# menu.append("PIZZA")
# print(menu)


# - insert()--->
# Kisi specific index par item add karta hai.

# menu1 = ["FRIES", "BURGER"]

# menu1.insert(0, "PIZZA")
# print(menu1)


# - extend()--->
# ek list mein multiple items add karne ke liye use hota hai.

# IMPORTANT:


# menu2 = ["FRIES", "BURGER"]

# menu2.extend(["PIZZA", "PASTA"])
# print(menu2)


# IMPORTANT:
# poori ["PIZZA", "PASTA"] ko one item samjhega.
# menu2.extend("PIZZA", "PASTA")

# ko separately add karega.
# menu2.extend(["PIZZA", "PASTA"])



# LIST REMOVAL METHODS:
# Python mein List se items remove karne ke 4 important ways hain.

# - remove()--->
# - pop()--->
# - del --->
# - clear --->

# LIST — REMOVING ITEMS

# 1. remove()
# - Removes an item by VALUE.
# - Removes only the first matching value.
# - Returns None.
# - Raises ValueError if value doesn't exist.

# Example:
# numbers = [10, 20, 10, 30]
# numbers.remove(10)
# # [20, 10, 30]


# 2. pop()
# - Removes an item by INDEX.
# - Returns the removed item.
# - Without an index, removes the last item.

# Example:
# numbers = [10, 20, 30]
# x = numbers.pop(1)
# # x = 20
# # numbers = [10, 30]


# 3. del
# - Deletes item(s) by index or slice.
# - Can also delete the entire list variable.
# - Does not return the removed item.

# Example:
# numbers = [10, 20, 30]
# del numbers[1]
# # [10, 30]


# 4. clear()
# - Removes ALL items from the list.
# - The list itself remains.
# - Result is an empty list.

# Example:
# numbers = [10, 20, 30]
# numbers.clear()
# # []


# QUICK MEMORY:
# remove() → VALUE
# pop()    → INDEX
# del      → DELETE
# clear()  → ALL