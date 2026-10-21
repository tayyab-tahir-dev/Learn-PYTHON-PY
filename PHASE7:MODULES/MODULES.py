                                # <----------PHASE 7: MODULES---------->

# WHAT WE WILL COVER IN THIS SECTION:

# 1) Modules
# 2) import
# 3) pip
# 4) packages
# 5) virtual environment
# 6) uv
# 7) poetry (overview)


                                    # <----------MODULES---------->

# 1) - MODULE --->

# INTERVIEW DEFINATION:
# A module is a Python file containing code such as variables, functions, and classes.

# SIMPLE UNDERSTAND:
# Module aik Python file hoti hai jismein variables, functions aur classes ka code ho sakta hai.jinhein hum doosri Python files mein reuse kar sakte hain.

# EXAMPLE:

# def read_document():
#     return "Python is used in AI."

# IMPORTAND:
# MODULE FILE HOTI HAI NA KAY USKE ANDAR VALA ACTUAL CODE:



                                       # <----------IMPORT---------->

# 2) - import--->

# DEFINATION:
# import is a Python statement used to make a module available for use in another Python file.

# SIMPLE UNDERSTAND:
# import aik Python statement hai jo humein kisi module ka code apne program mein use karne deta hai.

# EXAMPLE:

# def read_documents():
#     return "Python is used in AI."


# - import---> (PART-2)

# from ... import
# Module ke andar se kisi specific function, variable ya class ko import karta hai.

# EXAMPLE:

# def greet(): 
#     return "Python is good in AIEngineering"


# - import---> (PART-3)
# as (Alias)

# as ki madad se hum imported module ya function ko aik doosra naam de sakte hain, jise alias kehte hain.

# EXAMPLE:

# def documet_reader():
#     return "HELLO WORLD"


# - import---> (PART-4)
# if __name__ == "__main__"

# Iska matlab hai ke kuch code sirf tab chale jab hum Python file ko directly run karay. Agar koi doosri file usay import kare, to woh specific code nahi chalega.

# EXAMPLE:

# def greet():
#     return "MODULE FILE CODE RUNNING."


# if __name__ == "__main__":
#     print(greet())


# EXPLANATION:
# Agar yeh file directly run ho, tab "MODULE FILE CODE RUNNING" print karo.

# Agar yeh file kisi doosri file se import ho, to is if ke andar wala code execute nahi hoga.

# Yaad rakhne wali baat: __name__ Python ka special variable hai, aur "__main__" ek string hai.


# - import---> (PART-5)
# Importing Variables:

# Kisi doosri Python file mein banaye gaye variable ko apni file mein use karna variable import karna kehlata hai.

# EXAMPLE"

# document_name = "AI_notes.pdf"


# - import---> (PART-6)
# Importing Functions

# Ek hi Python file se aik se zyada functions, variables ya classes ko ek hi statement mein import karna.

# EXAMPLE:

# model_name = "embedding-model"
# chunk_size = 5000

# def get_config():
#     return "Configuration Loaded"


# - import---> (PART-7)
# Importing a Class

# Kisi doosri Python file mein banayi gayi class ko apni file mein use karna class import karna kehlata hai.

# EXAMPLE:

# class DocumentReader:
#     def read(self):
#         return "Document read sucessfully."


# - import---> (PART-8)
# Module Caching

# Python aik module ko pehli baar load karne ke baad usay cache mein rakhta hai, taake dobara import karne par uska top-level code baar baar execute na ho.


# Har technical word ka matlab
# - Cache: Pehle se load ki hui cheez ko temporarily save rakhna.
# - Module: Python file, jaise config.py.
# - Top-level code: Woh code jo function ya class ke bahar likha ho.
# - Execute: Code ko chalana.

# EXAMPLE:

# print("HELLO FROM FIRST FILE.")


# - import---> (PART-9)
# sys.path

# sys.path un locations ki list hai jahan Python kisi module ko dhoondta hai jab hum import likhtay hai.

# 1. sys (System Module): Python ka built-in module jo Python interpreter aur system ke saath related information aur functions provide karta hai.

# Example: sys.version se Python ke version ki information milti hai.

# 2. path (Path): Kisi file ya folder ki location ka address.

# Example: "/home/tayyab/project/main.py" ek file ka path hai.

# EXAMPLE:
# ON SECOND FILE MODULES2.py


# - import--->  (PART-10)
# Common Import Errors aur Naming Conflicts