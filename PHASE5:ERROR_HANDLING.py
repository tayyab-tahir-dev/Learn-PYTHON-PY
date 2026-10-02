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