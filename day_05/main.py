import random
import string

print("\nWelcome to the PyPassword Generator!")

# Input for the number of letters, symbols, and digits
let = int(input("How many letters would you like in your password? \n"))
sym = int(input("How many symbols would you like? \n"))
num = int(input("How many numbers would you like? \n"))

# Create a list for alphabets (letters)
alphabets = list(string.ascii_letters)
random.shuffle(alphabets)

# Create a list for symbols (punctuation)
symbols = list(string.punctuation)
random.shuffle(symbols)

# Create a list for digits
digits = list(string.digits)
random.shuffle(digits)

# Create the password components
new_a = []

for i in alphabets[:let]:
    new_a.append(i)

for a in symbols[:sym]:
    new_a.append(a)

for x in digits[:num]:
    new_a.append(x)

# Shuffle the final list of characters to ensure randomness
random.shuffle(new_a)

# Join the list into a string
password = ""
for p in new_a:
    password += p

print(f"\nYour password is: {password}\n")
