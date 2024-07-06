import random

# Character pool to create passwords from
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\"

print(" ") # Gap for readability in terminal

amount = int(input("Enter the amount of passwords to generate: "))

print(" ") # Gap for readability in terminal

# Function to create passwords
for a in range(amount):
    password = ""

    length = int(input("Enter password length: "))

    print(" ") # Gap for readability in terminal

    for c in range(length):

        password += random.choice(chars) 

    print(password)
    
    print(" ") # Gap for readability in terminal
