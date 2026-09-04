                  # <----------PHASE 2: COLLECTION:---------->


# LIST

# INTERVIEW STYLE DEFINATION:
# A Python list is an ordered, mutable collection that can store multiple items, including 
# duplicates and different data types.

# SIMPLE UNDERSTANDING:
# List Python mein ek ordered aur mutable collection hai jo multiple items ko store karti hai.

# SYNTAX:
# my_list = ["item1", "item2", "item3"]


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


# - TUPLE PACKING--->:
# Multiple values ko tuple mei group/pack karna:

# EXAMPLE:

# a = 10, "Tayyab", True, 20

# print(a)

# Yha pr multiple values ko aik single tuple mai pack kr dia.



# - TUPLE UNPACKING--->:
# Ek tuple ke multiple values ko ek hi waqt mein multiple variables mein assign karna.

# EXAMPLE:
# user_id = ("TAYYAB", 18, "PAKISTAN")

# user, age, country = user_id

# print(user)
# print(age)
# print(country)

# OUTPUT:
# TAYYAB
# 18
# PAKISTAN

# YHA PR UNPACK HO KR USER MULTIPLE VARIABLES MAY ASSIGN KR DIA:



# -TUPLE KA REAL-WORLD USE CASE:
# Tuple tab useful hoti hai jab data ka structure fixed ho aur tum nahi chahte ke values 
# accidentally modify ho jayein.

# Example:
# location = (31.5204, 74.3587)

# Latitude aur longitude ka fixed pair.

# Ya:

# rgb = (255, 128, 0)

# RGB values ka fixed set.

# Ya database se kisi record ka fixed structure:

# user = (101, "Ali", "ali@example.com")


 
                              # <--------SET-------->


# - SET--->:

# INTERVIEW STYLE Definition:
# A set is an unordered, mutable collection of unique elements.

# SIMPLE UNDERSTANDING:
# Set Python mein ek unordered aur mutable collection hai jo sirf unique elements ko store karta
# hai.

# SYNTAX:

# my_set = {"item1", "item2", "item3"}



# Properties:
# - Unordered
# - Mutable
# - Does NOT allow duplicates
# - No indexing
# - No slicing
# - Supports membership testing
# - Elements must be hashable

# Syntax:
# my_set = {1, 2, 3}

# Empty Set:
# set() → empty set
# {}    → empty dictionary

# Adding:
# add()    → adds one element
# update() → adds multiple elements

# Removing:
# remove()  → removes specified element
#              missing element → KeyError

# discard() → removes specified element
#              missing element → no error

# pop()     → removes and returns an arbitrary element

# clear()   → removes all elements

# Set Operations:
# |  → Union
# &  → Intersection
# -  → Difference
# ^  → Symmetric Difference

# Other:
# issubset()    → checks subset
# issuperset()  → checks superset
# isdisjoint() → checks no common elements

# Important:
# Set does not support indexing or slicing.

# Set automatically stores only unique elements.
# Isi wajah se Set real programming mein bohot useful hai.


# - Set ka sabse important feature--->:
# Unique Values:

# Set duplicates ko allow nahi karta.

# numbers = {10, 20, 30, 10, 20, 30, 40, 50}
# print(numbers)

# OUTPUT:
# {50, 20, 40, 10, 30}


# - Set unordered hota hai--->;

# numbers = {10, 20, 20}
# print[numbers[0]]

# Yeh nhi kr sktay q kay set unordered hai.
# Set indexing aur slicing support nahi karta.

# Kyukay?
# Kyuke Set ka purpose position-based access nahi hai.

# Set ka main focus hai:
# Uniqueness + fast membership checking.


# - Important modern Python point--->:

# Set ka output kabhi kisi particular order mein appear ho sakta hai, lekin us order par depend 
# nahi karna chahiye.


# - SET mutable hota hai--->:

# Set ke elements ko individually index ke through modify nahi kar sakte, lekin Set ke contents ko 
# change kar sakte ho.

# - EMPTY SET--->:

# data = set()
# print(type(data))

# SIMPLE:
# set() → empty set
# {}    → empty dictionary


# - METHODS IN SET--->:

# - ADDING METHOD--->:
# 1) add()

# Set mein item add karna.
# AIk item add karne ke liye.

# EXAMPLE:

# fruits = {"Apple", "Mango", "Orange"}

# fruits.add("Banana")
# print(fruits)

# OUTPUT:
# {'Orange', 'Apple', 'Mango', 'Banana'}


# 2) update()
# Multiple items add krnay kay liyay:

# numbers = {10, 20, 30,}

# numbers.update([40, 50, 60])
# print(numbers)

# OUTPUT:
# {40, 10, 50, 20, 60, 30}


# - REMOVING METHOD--->:

# 1) remove()
# Set se specific value remove karne ke liye. 

# EXAMPLE:

# users = {"Tayyab", "Taha", "Ali"}

# users.remove("Tayyab")
# print(users)

# OUTPUT:
# {'Taha', 'Ali'} 

# AGHAR VALUE EXIST NHI KRTI TOH ERROR AAYEGA:

# 2) discard()
# Set se specific value remove karne ke liye.

# EXMAPLE:

# numbers = {10, 20, 30, 40, 50}

# numbers.discard(40) 
# print(numbers)

#OUPUT: 
# {50, 20, 10, 30}

# AGHAR VALUE EXIST NHI KRTI TOH BHI ERROR NHI AAYEGA:


# 3) pop()
# Set se random value remove karne ke liye.
# OR us value ko return karne ke liye.  

# EXAMPLE:

# values = {10, 20, 30, 40, 50}

# removed_value = values.pop()

# print(removed_value)

# print(values)


# 4) clear()
# Set se saari values remove karne ke liye.

# EXAMPLE:

# users = {"Tayyab", "Taha", "Ali"}

# users.clear()
# print(users)

# OUTPUT:
# set()



# - Set Operations--->:

# SET KA SUB SAY POWERFUL FEATURE HAI.
# Sets mathematical set operations support karte hain:

# |  → Union         → Do sets ke all unique elements combine karta hai.
# &  → Intersection  → Dono sets mein jo elements common hain:
# -  → Difference    → Pehle Set mein jo hain, lekin doosre Set mein nahi:
# ^  → Symmetric Difference → Jo elements dono mein hain unko hata kar sirf non-common elements:

# IS TARAH BI KR SKTAY HAI:
# A.union(B)
# A.intersection(B)
# A.difference(B)
# A.symmetric_difference(B)

# OR 

# IS TARAH BHI:
# A | B
# A & B
# A - B
# A ^ B


# 1) Union → |
# Do sets ke all unique elements combine karta hai:

# EXAMPLE:

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)

# OUTPUT:
# {1, 2, 3, 4, 5}



# 2) INTESECTION → &
# Dono sets mein jo elements common hain:

# EXAMPLE:

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a & b)

# OUTPUT:
# {2, 3}



# 3) DIFFERRENCE → -
# Pehle Set mein jo hain, lekin doosre Set mein nahi:

# EXAMPLE:

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a - b)

# OUTPUT:
# {1}



# 4) SYMMETRIC DIFFERRENCE → ^
# Jo elements dono mein hain unko hata kar sirf non-common elements.
# NON-COMON MTLB:
# Jo elements dono sets mein same nahi hai, yani sirf ek set mein present hain.
# JASAY.

# EXMAPLE:

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a ^ b)

# OUTPUT:
# {1, 4}


# - SET COMPARISON--->:
# Set comparison mein 3 important methods hain:

# 1) issubset() → checks subset
# 2) issuperset() → checks superset
# 3) isdisjoint() → checks no common elements

# 1) issubset() → checks subset
# Agar set A ka saara data set B mein exist karta hai to A, B ka subset hai.
# Agar A ka saara data B mein exist nahi karta to A, B ka subset nahi hai.

# EXAMPLE:

# a = {1, 2, 3}
# b = {1, 2, 3, 4, 5}

# print(a.issubset(b))

# OUTPUT:
# True


# 2) issuperset() → checks superset
# Aghar set b ka saara data set A mein exist karta hai to A, B ka superset hai.
# Agar B ka saara data A mein exist nahi karta to A, B ka superset nahi hai.

# EXAMPLE:

# a = {1, 2, 3, 4, 5}
# b = {1, 2, 3}

# print(a.issuperset(b))

# OUTPUT:
# True


# 3) isdisjoint() → checks no common elements
# Agar dono sets mein koi common element nahi hai to True return karega.
# Agar dono sets mein koi common element hai to False return karega.

# EXAMPLE:

# a = {1, 2}
# b = {3, 4}

# print(a.isdisjoint(b))

# OUTPUT:
# True

# SET KUB USE KRNA CHAHIYE:
# Set tab use karo jab hamay unique values chahiye hon ya membership checking karni ho or hamay
# index-based access ki zarurat na ho.



                              # <-----DICTIONARY----->

# - WHAT IS DICTIONARY--->:

# INTERVIEW STYLE DEFINATION:
# A dictionary is a unordered/mutable collection of key-value pairs where each key is unique and used to 
# access its corresponding value.

# SIMPLE UNDERSTANDING:
# Dictionary ek unordered/mutable collection hai jo key-value pairs store karti hai, jahan har key unique 
# hoti hai aur us key ke through value access ki jati hai.

# EXMAPLE:

# user = {
#     "name": "Tayyab",
#     "age": 18,
#     "course": "Python"
# }

# print(user["name"])
# print(user["age"])
# print(user["course"])

# OUPUT:
# Tayyab
# 18
# Python

# REASON:

# "name"    → key
# "Tayyab"  → value
# "age"     → key
# 18        → value
# "course"  → key
# "Python"  → value

# Dictionary mein data ko index se nahi, key se identify/access kiya jata hai.


# - SYNTAX--->:
# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }


# { }   → dictionary ko represent karte hain
# :     → key aur value ko separate karta hai
# ,     → multiple pairs ko separate karta hai

# EMPTY DICTIONARY:
# my_dict = {}