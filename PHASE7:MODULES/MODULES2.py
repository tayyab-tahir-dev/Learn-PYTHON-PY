# 2) - import--->
# EXAMPLE:


# import MODULES

# result = MODULES.read_documents()
# print(result)


# (PART-2) 
# from ... import

# EXAMPLE:


# from MODULES import greet

# result = greet()
# print(result)



# DONO KA ACTUAL DIFFENENCE:

# import	                                                                            from ... import
# import document_reader                                                                from document_reader import read_document
# Function ko document_reader.read_document() se call karte hain	                    Function ko read_document() se call karte hain
# Module ka naam visible rehta hai	                                                    Imported function ko directly access karte hain


# (part-3)
# as (alias)

# EXAMPLE:

# import MODULES as he

# result = he.documet_reader()
# print(result)


# (PART-4)
# if __name__ == "__main__"

# EXAMPLE:

# import MODULES

# print("MODULE 2 FILE CODE RUNNING.")


# (PART-5)
# Importing Variables:

# EXAMPLE:

# from MODULES import document_name

# print(document_name)


# (PART-6)
# Importing Functions:

# EXAMPLE:

# from MODULES import model_name, chunk_size, get_config

# print(model_name)
# print(chunk_size)
# print(get_config())


# (PART-7)
# Importing a Class:

# EXAMPLE:

# from MODULES import DocumentReader

# reader = DocumentReader()
# print(reader.read())


# (PART-8)
# Module Caching:

# EXAMPLE:

# import MODULES
# import MODULES

# print("HELLO FROM SECOND FILE.")


# (PART-9)
# sys.path:

# EXAMPLE:
# import sys

# print(sys.path)


# (PART-10)
# Common Import Errors aur Naming Conflicts