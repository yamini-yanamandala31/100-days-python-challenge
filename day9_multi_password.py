import random
import string

count = int(input("How many passwords you want? "))
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print("Password", i+1, ":", password)
