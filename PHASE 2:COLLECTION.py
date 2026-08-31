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
# - clear() --->


# LIST — REMOVING ITEMS

# 1) - remove()--->
# - Removes an item by VALUE.
# - Removes only the first matching value.
# - Returns None.
# - Raises ValueError if value doesn't exist.

# Example:
# numbers = [10, 20, 10, 30]

# numbers.remove(10)
# print(numbers)

# OUTPUT:
# [20, 10, 30]

# EXAMPLES:
# students = ["Ali", "Ahmed", "Tayyab"]

# students.remove("Ahmed")
# print(students)

# OUTPUT:
# ["ALI", "TAYYAB"]


# 2) - pop()--->
# - Removes an item by SPECIFIC INDEX.
# - Returns the removed item.
# - Without an index, removes the last item.

# Example:
# numbers = [10, 20, 30]

# numbers.pop(1) 
# print(numbers)

# OUTPUT:
# [10, 30]

# EXAMPLE:
# students = ["Ali", "Ahmed", "Tayyab"]

# students.pop(1)
# print(students)

# OUTPUT:
# ["Ali", "Tayyab"]


# RETURNS THE REMOVED ITEM:
# students = ["Ali", "Ahmed", "Tayyab"]

# removed_student = students.pop(1)
# print(removed_student)
# print(students)

# Agar index nahi doge to last item remove hoga.

# students = ["Ali", "Ahmed", "Tayyab"]

# students.pop()
# print(students)


# 3) - del--->
# - Deletes item(s) by index or slice.
# - Can also delete the entire list variable.
# - Does not return the removed item.

# Example:
# numbers = [10, 20, 30]
# del numbers[1]

# OUTPUT:
# # [10, 30]


# students = ["Ali", "Ahmed", "Tayyab"]

# del students[1]
# print(students)

# OUTPUT:
# ["Ali", "Tayyab"]


# SLICING KAY SAT MULTIPLE ITEMS REMOVE:
# numbers = [10, 20, 30, 40, 50, 60]

# del numbers[1:4]
# print(numbers)

# OUTPUT:
# [10, 50, 60]


# students = ["Ali", "Ahmed", "Tayyab"]

# del students[1:2]
# print(students)

# OUTPUT:
# ["Ali", "Tayyab"]


# Puri list ka variable bhi delete kar sakte hai:

# numbers = [10, 20, 30]

# del numbers

# Ab numbers variable exist nahi karega.

# Important difference
# del removed item ko return nahi karta.


# 4) - clear()--->
# - Removes ALL items from the list.
# - The list itself remains.
# - Result is an empty list.

# Example:
# numbers = [10, 20, 30]
# numbers.clear()
# print(numbers)

# OUTPUT:
# []


# QUICK MEMORY:
# remove() → VALUE
# pop()    → INDEX
# del      → DELETE
# clear()  → ALL




                           # <----------TUPLE---------->


# INTERVIEW STYLE DEFINATION:
# In PYTON A TUPLE is an ordered and immutable collection used to store multiple items.

# SIMPLE UNDERSTANDING:
# TUPLE PYTHON mai aik ordered aur immutable collection hai jo multiple items ko store karti hai.

# SYNTAX:
# my_tuple = ("item1", "item2", "item3")


# Properties:
# - Ordered
# - Immutable
# - Allows duplicates
# - Can store different data types
# - Supports indexing
# - Supports negative indexing
# - Supports slicing
# - Uses ()

# Important Methods:
# count() → counts occurrences of a value
# index() → returns first index of a value

# Single-item tuple:
# (10,) → tuple
# (10)  → int

# Tuple Packing:
# x = 10, 20, 30

# Tuple Unpacking:
# a, b, c = (10, 20, 30)

# Important:
# Tuple cannot be directly modified,
# added to, or have items removed.

# Use Tuple:
# When data is ordered and should remain unchanged.



# - ORDERED--->:
# LIST ki tarah TUPLE bi ORDERED hoti hai.

# EXAMPLE:
# colors = ("Red", "Orange", "Purple")

# print(colors[0])

# OUTPUT:
# RED


# red    → 0
# green  → 1
# blue   → 2


# - IMMUTABLE--->:
# Yeh TUPLE ka sabse important concept hai.

# Immutable ka matlab:

# Tuple create hone kay baad uskay elements ko directly change, add ya remove nhi kar saktay.

# EXAMPLE:

# colors = ("red", "green", "blue")

# colors[0] = "yellow"
# print(colors)


# Yha error a jay ga q kay TUPLE IMMUTABLE hai.
# COMPARE TO LIST: LIST may error nhi aya ga q kay vo MUTABLE hai.


# - ALLOW DUPLICATES--->:
# TUPLE mein same value multiple times aa sakti hai.

# EXAMPLE:

# numbers = (10, 20, 10, 20, 30, 40, 50, 30)
# print(numbers)


# - They can store different DATATYPES--->:
# TUPLE mein different data types bhi store ho sakte hain:

# EXAMPLE:
# data = ("Tayyab", 3.23, 10, True)
# print(data)

# OUTPUT:
# ("Tayyab", 3.23, 10, True)


# - POSITIVE INDEXING--->:
# TUPLE may items indexing say access kr sktay hai.

# EXAMPLE:
# data = ("Ali", "Ahmad", "Tayyab")

# print(data[0])
# print(data[1])
# print(data[2])

# OUTPUT:
# Ali
# Ahmad
# Tayyab


# - NEGATIVE INDEXING--->:
# NEGATIVE INDEXING -1 say start hoti hai.

# EXAMPLE:
# data1 = ("Ali", "Ahmad", "Tayyab")

# print(data1[-1])
# print(data1[-2])
# print(data1[-3])

# OUTPUT:
# Tayyab
# Ahmad
# Ali


# - SLICING--->:
# TUPLE may slicing differrnt hai yeh hamay vo items retun krti hai na kay list ki tarah delete.

# SYNTAX:
# tuple[start:stop]
# stop index include nahi hota.

# EXAMPLE:
# items = ("Laptop", "KeyBoard", "Mouse", "Mobile", "Usb", "LCD")

# print(items[1:3])

# OUTPUT:
# ('KeyBoard', 'Mouse')



# numbers = (10, 20, 30, 40, 50)

# print(numbers[1:4])

# OUTPUT:
# (20, 30, 40)


# - TUPLE MAY 2 MAIN BUILT-IN METHODS HAI--->:

# 1) count() → VALUE KITNI BAAR AYI HAI.
# 2) index() → VALUE KA FIRST INDEX.

# 1) count()
# BTATA HAI KAY VALUE KITNI BAAR AYI HAI TUPLE MAY.

# EXAMPLE:
# numbers = (10, 20, 30, 40, 10, 50, 10)

# print(numbers.count(10))

# OUTPUT:
# 3


# 2) index()
# BTATA HAI KAY VALUE KA FIRST INDEX KYA HAI.

# EXAMPLE:

# numbers1 = (10, 20, 30, 40, 10, 50, 10)

# print(numbers1.index(10))



# - SINGLE-ITEM TUPLE--->:
# Python mein SINGLE-ITEM TUPLE ka main use yeh hota hai ke hum sirf ek value ko tuple ke form 
# mein store kar saken.

# IMPORTANT:
# SINGLE-ITEM TUPLE banane ke liye comma zaroori hai:
# EXAMPLE:

# Bagar comma (,) kay yeh simple integer hai:
# Python isko simply integer samjhega.
# x = (10)
# print(type(x))


# Yeh real way hai single-item tuple create krnay ka:
# COMMA (,) kay sat
# x = (10,)
# print(type(x))


# - TUPLE WITHOUT PARENTHESES--->:
# Python mein parentheses technically mandatory nahi hain.
# Hum PARENTHESES kay bahgar bi code likh sktay hai lekin tuple kay case may comma ( , ) 
# important hai.

# EXAMPLE:

# numbers = 10, 20, 30
# print(numbers)
# print(type(numbers))


# MORE EXAMPLE:

# string = "TAHA", "ALI", "AHMAD"
# print(string)
# print(type(string))

# GOLDEN POINT:-
# Parentheses tuple banane ke liye optional ho sakte hain, lekin Python tuple ko display karte 
# waqt parentheses use karta hai.
# Mtlb output mai parentheses ata hai.

