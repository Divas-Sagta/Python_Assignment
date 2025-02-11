
# Write a Python program that generates a password with the following conditions:
# At least one uppercase letter.
# At least one lowercase letter.
# At least two numbers.
# At least one special character (e.g., !@#$%&*).
# The password should be exactly 16 characters long.
# The password should contain no repeating characters.
# The password should have a random order each time.


import random
import string

def generate_password():
    chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*")
    password_set = set()

    while len(password_set) < 16:
        password_set.add(random.choice(chars)) 

    password = list(password_set)
    random.shuffle(password)  

    return "".join(password)

print(generate_password())

