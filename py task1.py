import string
import random  

length = int(input("enter password length="))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

characters = letters+digits+symbols

password = ""

for i in range(length):
        password +=random.choice(characters)

print("generated password=",password)        