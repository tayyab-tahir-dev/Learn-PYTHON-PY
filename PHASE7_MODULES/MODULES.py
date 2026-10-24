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

# Jab Python ko required module nahi milta ya woh usay sahi tarah load nahi kar pata, to import error aa sakta hai.

# 1. ModuleNotFoundError
# Agar hamari file ka naam document_reader.py hai, lekin hum likhay:

# import documentreader

# To error aa sakta hai, kyun ke module ka naam galat likha hai.

# is liye file ka name sahi likho.


# 2. Naming Conflict
# Naming conflict ka matlab hai ke hamari file ka naam kisi Python ke built-in ya standard-library module ke naam se takra raha ho.

# Misal ke taur par, agar hum apni file ka naam random.py rakh dete hai:

# import random

# print(random.randint(1, 10))

# Python hamari apni random.py file ko import kar sakta hai, standard-library wale random module ki jagah. Is se unexpected errors aa sakte hain.

# Best way: Apni files ke naam random.py, json.py, ya sys.py jaise common module names na rakho.



                                        # <----------PACKAGE---------->

# 3) - Package--->

# INTERVIEW DEFINATION:
# A package is a way to organize related Python modules into a directory structure.

# SIMPLE UNDERSTAND:
# Package aik folder hota hai jisme related Python modules ko organize kiya jata hai, taake project ka code manage aur reuse karna asaan ho.


# ai_project/                  ← Main project folder
# │
# ├── main.py                  ← Module
# │
# └── document_tools/          ← Package
#     ├── document_reader.py   ← Module
#     ├── text_cleaner.py      ← Module
#     └── chunker.py           ← Module


# Module aur Package mein difference:


# Module = Python file

# Example: 
# AI_App.py
# Is file mein functions, variables aur classes ho sakti hain.


# Package = related modules ka folder

# Example: document_tools
# Is folder mein multiple Python files organize ki ja sakti hain.


# - Package---> (PART-2)
# __init__.py IN Package:

# Python mein commonly package folder ke andar __init__.py file rakhi jati hai.

# STRUCTURE:

# document_tools/
#     __init__.py
#     document_reader.py
#     text_cleaner.py


# EXPLANATIONS:

# __init__.py ka naam double underscores se shuru aur khatam hota hai.
# 1) - __init__ — initialization se related naam.
# 2) - .py — Python file ki extension.
# 3) - Is file ko package initialization ke liye use kiya ja sakta hai.
# 4) - Modern Python mein kuch packages __init__.py ke baghair bhi kaam kar sakte hain, lekin abhi hum regular package structure seekh rahe hain.

# Filhal sirf itna samjho: package related modules ko organize karta hai, aur __init__.py us package ka initialization point ho sakta hai.


# <---AGAY KUCH CONCEPTS PHASE7:_PACKAGES VALAY FOLDER MAI HAI--->


                                     # <----------VIRTUAL ENVIROMANT---------->

# 4) - Virtual Enviroment--->

# INTERVIEW DEFINATION: 
# A virtual environment is an isolated Python environment for a project, where its installed packages can be managed separately.

# SIMPLE UNDERSTAND:
# Virtual environment aik project ka alag Python environment hota hai, jahan us project ki libraries aur packages ko doosre projects se alag manage kar sakte hain.

# Iski zaroorat kyun hoti hai?

# Misaal ke taur par hum do AI projects bana rahe hai:

# - Project A: requests library ka version 2 use karta hai.
# - Project B: kisi doosre version par depend karta hai.

# Virtual environments dono projects ki dependencies ko alag rakhne mein madad karte hain, taake aik project ki library doosre project ko affect na kare.


# HOW TO MAKE AND ACTIVATE VIRTUAL ENVIROMENT:

# 1) JIS FOLDER MAI  VE BANAHA HAI USKAY  OPEN WITH  INTEGRATED TERMINAL MAI OPEN KRO:
# YEH COMMAND RUN KRO:

# python3 -m venv .venv

# Command ka matlab:
# - python3 — Python 3 interpreter.
# - -m — Python module ko program ki tarah run karna.
# - venv — Python ka built-in module jo virtual environment banata hai.
# - .venv — us folder ka naam jahan environment banega.


# 2) Environment activate karne ke liye:
# YEH COMMAND CHALAO:

# source .venv/bin/activate

# Activation ke baad terminal prompt ke start mein aam tor par (.venv) nazar aayega.

# 3) Check karne ke liye:
# YEH COMMAND RUN KRO:

# which python

# OUTPUT US FILE KI TARAF HOGA:

# 4) Deactivate kene ke liye:

# deactivate