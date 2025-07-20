# pasword genrator
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

length = int(input("Enter password length: "))

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)