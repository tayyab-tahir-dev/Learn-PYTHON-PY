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


                                        # <----------PIP---------->

# 5) - pip--->
# In Python, pip primarily stands for "Pip Installs Packages".

# INTERVIEW DEFINATION
# pip is Python’s package installer, used to install and manage external Python libraries.

# SIMPLE UNDERSTAND: 
# pip aik tool hai jis se hum Python mein doosron ki banayi hui libraries install karte hain.

# Example:
# Agar hum apne AI project mein Gemini API use karna chahay, to uski library install karne ke liye pip use kar sakte hai.

# python -m pip install google-genai

# Yeh command hamaray active virtual environment mein library install karegi.

# - python -m pip — Python ke through pip chalata hai.
# - install — package install karta hai.
# - google-genai — package ka naam hai.


# - pip---> (PART-2)
# pip package install karne ke baad kya hota hai?

# pip install requests — library install karta hai.

# import requests — library ko Python code mein use karne ke liye import karta hai.


# - pip---> (PART-3)
# pip freeze

# INTERVIEW DEFINATION:
# pip freeze displays the installed Python packages and their versions.

# SIMPLE UNDERSTAND:
# Yeh hamay Python environment mein installed packages aur unke versions ki list dikhata hai.

# EXAMPLE OUTPUT:

# google-genai==1.20.0
# requests==2.32.4


# google-genai — package ka naam.
# == — installed version ko show karta hai.
# 1.20.0 — package ka version number hai.


# AI project mein iska faida: 
# Tumhein pata chal sakta hai ke project mein kaun si libraries aur unke kaun se versions installed hain.


# - pip---> (PART-4)
# requirements.txt

# Yeh aik text file hoti hai jismein project ke liye zaroori Python libraries aur unke versions likhe hote hain.

# EXAMPLE:

# google-genai==1.20.0
# requests==2.32.4



# BOTH IN ONE LINE:

# pip freeze — installed packages ki list dikhata hai.

# requirements.txt — packages ki list ko file mein rakhta hai, taake project ki dependencies share ki ja saken.


                                            # <----------UV---------->

# 6) - uv--->

# INTERVIEW DEFINATION: 
# uv is a fast Python tool used to manage packages, dependencies, and virtual environments.

# SIMPLE UNDERSTAND:
# uv aik tool hai jo Python packages install karne aur virtual environments manage karne mein madad karta hai.

# pip aur uv mein farq

# pip	                                      uv
# Python packages install karta hai.	      Packages install kar sakta hai aur virtual environments bhi manage karta hai.
# Package management ke liye use hota hai.	  Kai Python project-management tasks aik hi tool se kar sakta hai.

# AI Engineering mein faida: 
# Jab hum RAG ya AI application banaye ge, to hamay multiple libraries install aur manage karni hongi. uv yeh kaam efficiently karne mein madad karta hai.


# - uv---> (PART-2)
# pip vs uv commands


# Dono se Python packages install kar sakte hi, lekin commands thori different hain.

# Kaam	
# pip                                                        	              uv
# Package install karna	python -m pip install requests	                      uv pip install requests
# Installed packages dekhna	python -m pip list	                              uv pip list
# Requirements file se install	python -m pip install -r requirements.txt  	  uv pip install -r requirements.txt



# MTLB AGHAR HAMARAY SYSTEM MAI uv INSTALL HAI TO Pip KI COMMAND BI RUN HO JAYE GI:


# - uv---> (PART-3)
# uv se virtual environment banana:

# uv venv

# Is command ka matlab:
# - uv — Python project manage karne wala tool.
# - venv — virtual environment banane ka command.
# - .venv — default environment folder ka naam



# FOR ACTIVATE uv 

# source .venv/bin/activate

# Is command ka matlab:
# - source — script ko current terminal session mein run karta hai.
# - .venv — virtual environment ka folder.
# - bin — Linux par environment ke executable programs ka folder.
# - activate — environment activate karne wali script.


# uv pip install kya hai:
# Is command se hum uv ki madad se apne Python environment mein libraries install karte hain.

# uv pip install requests



# COMMAND KA KAAM:

# uv — Python package aur project management tool.
# pip — package installation commands ka interface.
# install — package install karne ka action.
# requests — install hone wali library ka naam.


# uv pip install -r requirements.txt
# Is command se requirements.txt file mein likhi hui required libraries install hoti hain.

# uv pip install -r requirements.txt


# Is command ka kaam:
# uv — Python project management tool.
# pip install — packages install karne ke liye.
# -r — kisi file se requirements read karne ka option.
# requirements.txt — woh file jismein package names aur versions likhe hote hain.



                                         # <----------POETRY---------->

# 7) - portry--->
# Poetry aik tool hai jo Python project ki required libraries aur project settings ko manage karta hai.


# Poetry ka faida kya hai?
# Jab tum AI project banao ge, jaise RAG application, to usmein multiple libraries hongi. Poetry un libraries aur unke versions ko manage karne mein madad karta hai.


# Poetry mein do important files hain:

# - pyproject.toml — project ki configuration aur dependencies define karne ke liye.
# - poetry.lock — dependencies ke exact resolved versions record karne ke liye.



# BOTH IN ONE LINE

# pip      packages install karta hai.
# uv       packages aur environments manage kar sakta hai.
# Poetry   dependencies aur project configuration manage karta hai.


# SOME IMPORTAND COMMANDS 

# 1. python -m venv .venv — current folder mein .venv naam ka virtual environment banati hai.
# 2. source .venv/bin/activate — virtual environment activate karti hai.
# 3. deactivate — active virtual environment ko deactivate karti hai.
# 4. python -m pip install requests — requests library install karti hai.
# 5. python -m pip list — tumhare current Python environment mein installed packages aur unke versions ki list dikhati hai.
# 6. python -m pip freeze — installed packages aur unke versions ko package==version format mein dikhata hai. Is output ko requirements.txt mein save bhi kar sakte ho.
# Command 5 aur 6 mein farq:
# - pip list — packages ko readable table ki form mein dikhata hai.
# - pip freeze — packages ko requirements.txt jaisay format mein dikhata hai.


# - pyproject.toml---> (PART-2)
# Python project mein pyproject.toml ek configuration file hoti hai jo project ki settings aur dependencies ki information rakhti hai.

# IS NAME KA MTLB:

# py
# Python ko refer karta hai.

# project
# Hamara Python project.

# .toml
# File format ka extension hai. TOML ka full form Tom's Obvious, Minimal Language ha


# Is file mein kya likha hota hai?
# Example :

# [project]
# name = "my-ai-project"
# version = "0.1.0"
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]



# - poetry.lock---> (PART-3)
# Yeh file project ki installed hone wali dependencies ke exact versions record karti hai, taake project dobara setup karte waqt compatible package versions use kiye ja saken.


# - poetry commands---> (PART-4)

# poetry init

# Yeh command humse project ki information aur dependencies ke baare mein sawal karti hai, phir pyproject.toml banane mein madad deti hai.


# COMMAND KA WORK:

# Project ki configuration set karna.
# Dependencies define karne mein madad dena.
# pyproject.toml file create karna.



# poetry add
# Is command se hum apne project mein koi Python library add karte hai.

# poetry add requests

# Yeh Poetry project mein requests dependency add karta hai aur dependencies ko resolve karke lock file create ya update kar sakta hai.

# Important: Yeh commands Poetry ke workflow ke liye hain. Tumhare existing venv aur pip workflow mein inki zaroorat nahi.