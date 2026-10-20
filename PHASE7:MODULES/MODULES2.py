# 2) - import--->
# EXAMPLE:


# import MODULES

# result = MODULES.read_documents()
# print(result)


# (PART-1) 
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


# (part-2)
# as (alias)

# EXAMPLE:

# import MODULES as he

# result = he.documet_reader()
# print(result)


# (PART-3)
# if __name__ == "__main__"

# EXAMPLE:

# import MODULES

# print("MODULE 2 FILE CODE RUNNING.")