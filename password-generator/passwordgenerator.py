import random 
import string

def input_ctrl(promt):
    while True:
        try:
            value = int(input(promt))
        except ValueError:
            print("Please enter a valid number")
            continue

        if value < 4:
            print("Please enter a number greater than or equal to 4")
            continue
        
        return value
    
def password_strength(password):
    score = 0
    length = len(password)

    if length >= 8:
        score += 2
    if length >=12:
        score += 3
    if length >= 16:
        score += 4

    lower = sum(c.islower() for c in password)
    upper = sum(c.isupper() for c in password)
    numbers = sum(c.isdigit() for c in password)
    symbols = sum(c in string.punctuation for c in password)
    
    score += min(lower, 2)
    score += min(upper, 2)
    score += min(numbers, 2)
    score += min(symbols, 3)

    if score < 6:
        return("Very weak")
    elif score <10:
        return("Weak")
    elif score < 14:
        return("Strong")
    else:
        return("Very strong")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = string.punctuation

while True:
    length = int(input_ctrl("Enter number for password length (min. 4): "))


    all_characters = upper + lower + number + symbols
    password = "".join(random.choices(all_characters, k=length))
    print("Generated Password:", password)
    print(f"Password strength: {password_strength(password)}")

    keep_going = input("\nWant to generate another password (y/n)? ").lower()

    if keep_going == "y":
        continue
    else:
        break

