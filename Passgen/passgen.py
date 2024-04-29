import random

print(" ")
amount = int(input("Enter the amount of passwords to generate: "))
print(" ")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\"

for a in range(amount):
    password = ""
    length = int(input("Enter password length: "))
    print(" ")
    for c in range(length):
        password += random.choice(chars)
    print(password)
    print(" ")

