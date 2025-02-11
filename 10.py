
"""
Logic:

:   If a tuple contains a mutable object (like a list), we can modify 
    that mutable object without modifying the tuple itself.

"""


# Tuple containing a list as an element
my_tuple = (10, [20, 30, 40], "Python")


# Changing 20 to 50   
my_tuple[1][0] = 50  


# Printing the modified tuple
print(my_tuple)  
