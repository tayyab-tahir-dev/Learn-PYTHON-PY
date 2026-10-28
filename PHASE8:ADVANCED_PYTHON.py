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

# - List Comprehension--->

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


# SIMPLE UNDERSTAND:

# numbers = [1, 2, 3, 4, 5,]

# square = [number **2 for number in numbers]

# print(square)



# - number ** 2 har number ka square nikalta hai.
# - for number in numbers numbers ko ek ek karke leta hai.
# - squares mein results ki nayi list banti hai.