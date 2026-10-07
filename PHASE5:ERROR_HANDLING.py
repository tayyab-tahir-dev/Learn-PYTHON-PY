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

# 2) - except--->

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



# MULTIPLE EXCEPTIONS:
# Kabhi application mein different errors aa sakte hain:
# EXAMPLE:


# try:
#     number = int(input("Enter Number: "))

# except ValueError:
#     print("Please enter a valid number.")

# except TypeError:
#     print("Invalid data type.")

# Ab har exception ka apna handler hai.


# BONUS EXAMPLE:

# try:
#     number = int(input("Koi number enter karein jo 10 se divide ho: "))
#     result = 10 / number
#     print(f"Result : {result}")
# except ZeroDivisionError:
#     print("Error: Aap kisi bi number ko 0 se divide nhi kar sakte!")
# except ValueError:
#     print("Error: Please sirf valid number enter karein, ABCD nhi!")


                                            # <----------FINALLY---------->

# 3 - finally--->

# INTERVIEW DEFINATION:
# finally is a block that runs whether an exception occurs or not.

# SIMPLE UNDERSTAND:
# Error aaye ya na aaye, finally ka code run hoga.


# 🧠 try + except + finally
# teenon ka role:


# try:
#     risky code

# except ValueError:

#     aghar ValueError aaye

# finally:
#     error aye ya na aye 
#     yeh code chalega he chalega


# 🤖 Real AI Engineering Example

# Suppose AI application kisi resource ko use kar rahi hai aur operation ke baad cleanup karna hai.
# EXAMPLE:

# try:
#     print("Processing document...!")

# except:
#     print("Processing failed")

# finally:
#     print("Cleaning up resourse...!")


# Yahan finally ka use cleanup type ke kaam ke liye common hai.
# Real applications mein cleanup ka matlab ho sakta hai:

# resource close karna
# temporary data clean karna
# connection release karna


# EXAMPLE WITH RETURN:

# def check_finally():
#     try:
#         print("1. Mai try block ke andar hu.")
#         return "TRY KA RETURN"  # Yahan se function ko khatam ho jana chahiye
#     except:
#         print("Mai except block kay andar hu")
#         return "EXCEPT KA RETURN"
#     finally:
#         print("2. Mai finally block hu aur mai peeche nahi hatunga!")

# # Function ko call karte hain aur uska return value print karte hain
# result = check_finally()
# print(f"3. Function ne return kiya: {result}")


# SIMPLEST EXAMPLE TO UNDERSTAND FINALLY:
# ATM EXAMPLE: 


# try:
#     print("Transaction start")

#     number = int(input("Enter amount: "))

#     print("Transaction sucessful")

# except ValueError:
#     print("Invalid amount")

# finally:
#     print("Transaction process finished")


                                           # <----------raise----------->

# 4) - RAISE--->

# INTERVIEW DEFINATION:
# raise is used to manually trigger an exception in Python.

# SIMPLE UNDERSTAND:
# Hum khud apni condition ke basis par jaan bhooj kr error generate karta hai.


# IMPORTANT:

# raise se hum Python ko batate hain: "Suno, yeh galti hai!

# try-except se hum batate hain: "Agar aisi galti ho jaye, toh screen par user ko aasan lafzon mein samjha do.


# BASIC EXAMPLE:

# age = 15

# if age < 18:
#     raise ValueError("Age must be 18 or above")


# EXAMPLE WITH raise + try/except:

# try:
#     age = 15

#     if age < 18:
#         raise ValueError("Age must be 18 or above")

# except ValueError:
#     print("Invalid age")


# 🤖 REAL AI-EXAMPLE:

# try:
#     prompt = ""

#     if not prompt:
#         raise ValueError("Prompt cannot be empty")

#     print("Sending prompt to AI model...")

# except ValueError as error:
#     print(error)


# class InsufficientFundError(Exception):
#     def __init__(self, message="Balance ham hai!"):
#         self.message = message

#         super().__init__(self.message)

# current_balance = 500
# withdraw_amount = 1000

# if current_balance < withdraw_amount:
#     raise InsufficientFundError()
# else:
#     print("Transaction successful")


# AI Engineering mein iska fayda

# Tum application mein business/application rules enforce kar sakte ho.

# Example:

# Empty prompt
# Invalid configuration
# Invalid input
# Missing required value
# Unsupported operation


                                           # <----------CUSTOM EXCEPTIONS---------->

# 5) - CUSTOM EXCEPTIONS--->

# INTERVIEW DEFINATION:
# A custom exception is a user-defined exception created for a specific application error.

# SIMPLE UNDERSTAND:
# Hum apni application ke specific error ke liye apna khud ka exception type banate hain.


# class InvalidPromptError(Exception):
#      pass

# Bas itna code ek custom exception banane ke liye enough hai.

# Iska matlab hai:
# InvalidPromptError naam ki apni exception class banao.


# BASIC EXAMPLE:

# class InvalidPromptError(Exception):
#     pass


# try:
#     prompt = ""
#     if not prompt:
#         raise InvalidPromptError("Prompt cannot be empty")

# except InvalidPromptError as error:
#     print(error)



# 🤖 Real AI Engineering Example:

# Suppose hum RAG application bana rahe hai.
# RAG system ko search karne ke liye documents chahiye.

# Agar knowledge base mein koi document he nahi hai, to hum apna specific error bana sakte hai:


# class  KnowledgeBaseEmptyError(Exception):
#     pass


# try:
#     documents = []

#     if not documents:
#         raise KnowledgeBaseEmptyError("Khowledge base in empty")
    
#     print("Knowlegde base is ready")

# except KnowledgeBaseEmptyError as error:
#     print(error)


# AI Engineer ke perspective se:

# Jab application mein koi domain-specific problem ho jise clearly identify aur handle karna ho, custom exception useful hoti hai.



                                         # <----------LOGGING---------->

# 6) - LOGGING--->
