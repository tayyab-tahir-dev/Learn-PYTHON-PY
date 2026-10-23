# - PACKAGES--->

# EXAMPLE:

# from document_tools.document_reader import read_document

# result = read_document()
# print(result)


# EXPLANATION:
# read_document vala funtion yha use ho rha hai:JO document_reader file mai hai.

# - PACKAGES---> (PART-2)
# Aik package ke multiple modules use karna

# EXAMPLE:

# from document_tools.document_reader import read_document
# from document_tools.text_cleaner import clean_text


# result = read_document()
# cleaned_text = clean_text("   Python is used in AI.    ")

# print(result)
# print(cleaned_text)


# EXPLANATION:
# yha pr document_reader vali file ka function read_document or text_cleaner vali file ka clear_text function use ho rha hai.


# - PACKAGES---> (PART-3)

# __init__.py

# Python package ke initialization ke liye is file ko use kiya ja sakta hai. Abhi hum isay use karke package se function import karna seekhenge.

# EXAMPLE:

# from document_tools import read_document, clean_text

# result = read_document()
# cleaned_text = clean_text("     Python is used in AI.     ")

# print(result)
# print(cleaned_text)


# EXPLANATION:

# Pehle hamay module ka naam bhi likhna padta tha:

# from document_tools.document_reader import read_document

# Ab __init__.py ki madad se:

# from document_tools import read_document

# Yani package ke through functions ko seedha import kar sakte ho.

# Ab yeh code run karo aur batao output sahi aaya ya nahi.


# - PACKAGES---> (PART-4)

# Absolute Import vs Relative Import
# Python mein package ke andar modules import karne ke do common tareeqe hain.