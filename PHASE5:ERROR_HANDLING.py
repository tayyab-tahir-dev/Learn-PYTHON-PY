                             # <----------PHASE 5: ERROR_HANDLING---------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1) try
# 2) except
# 3) finally
# 4) raise
# 5) custom exceptions
# 6) logging


                                        # <----------ERROR-HANDLING---------->

# 0) - ERROR HANDILING--->

# Error Handling kya hota hai?
# ERROR HANDLING ka mtlb hota hai program mai aane wale errors ka properly handle krna,taake program achanak crash na ho.


# AI Engineering mein Error Handling

# Real AI application mein errors aa sakte hain:

# API request fail ho jaye
# API key invalid ho
# File missing ho
# User invalid input de
# Database connection fail ho
# LLM response expected format mein na aaye
# JSON parsing fail ho
# Internet/API timeout ho


                                            # <----------TRY---------->

# 1) - try --->

# INTERVIEW DEFINATION:
# try is used to wrap code that may raise an exception.

# SIMPLE UNDERSTAND:
# try ke andar hum woh code rakhte hain jisme error aane ka possibility ho.


# Yani hum Python ko basically keh rahe hote hain:

# Is code ko run karo, lekin agar ismein error aaye to usko hum properly handle karenge.

# SYNTAX:

# try:
#     risky code


# Lekin normally try ke saath except bhi hota hai:


# try:
#     risky code

# except:
#     error handle karne wala code


# BASIC EXAMPLE:


# try:
#     number = int("abc")
#     print(number)


# YAHAN:

# int("abc")

# risky operation hai.

# Python "abc" ko integer mein convert nahi kar sakta, isliye exception generate hogi.


# Important

# try ka kaam error ko fix karna nahi hai.

# try ka kaam hai:

# Potentially problematic/risky code ko identify karke usay try block mein rakhna.

# Actual handling hum except krta hai.


# REAL AI-EXAMPLE:

# AI application mein hum LLM API call kar sakte hain:


# try:
#     response = llm.generate(prompt)

#     print(response)


# Yahan API/LLM request risky operation hai.

# Possible problems:

# API request fail
# Network problem
# Timeout
# Invalid configuration
# Server error

# Hum in problems ko next concepts ke through properly handle karenge.

# 🧠 AI Engineer Mindset

# Jab bhi real application bana rahe ho, automatically yeh socho:

# "Is operation mein error aa sakta hai?"

# Agar answer yes hai, to us operation ko appropriate error-handling strategy ke andar rakhna chahiye.

# Examples:

# File Reading       → risky
# API Request        → risky
# Database Query     → risky
# JSON Parsing       → risky
# LLM Response       → potentially risky
# User Input         → potentially risky



                                           # <----------EXCEPT---------->

# - except--->

# INTERVIEW DEFINATION:
# except is used to catch and handle an exception raised inside the try block.

# SIMPLE UNDERSTAND:
# Agar try ke andar error aaye, to us error ko handle karne ke liye except use hota hai.


# SYNTAX:

# try:
#     risky code
# except:
#     error handle karne wala code


# BASIC EXAMPLE:

# try:
#     numbers = int("abc")
# except:
#     print("Something went wrong")


# YAHAN:
# int("abc")

# error generate karega.

# Python try ke andar error dekhega aur phir except ke andar chala jayega.

# Output:

# Something went wrong

# Is tarah program error ki wajah se simply crash hone ke bajaye error ko handle kar sakta hai.


# Specific Exception Handle Karna:
# Real Python code mein sirf:

# except:

# likhne ke bajaye specific error handle karna better hota hai.
# EXAMPLE:

# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("Sirf number enter karo.")

# YAHAN:

# Input mai interger ki jagah aghar "abc" de day to ValueError a skta hai:

# IS LIYE:
# Hum kehtay hai.

# except ValueError:

# Yaani aghar ValueError aye, to yeh code run kro:


# 🤖 REAL AI-EXAMPLE:

# Suppose AI application JSON response process kar rahi hai:

# import json

# response = '{"answer": "Python is easy"}'

# try:
#     data = json.loads(response)
#     print(data["answer"])

# except json.JSONDecodeError:
#     print("Invalid AI response format")