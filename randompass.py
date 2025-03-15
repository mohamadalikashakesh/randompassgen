import random
import string

#print lower
#ask user for upper , special , digits, length
#if length < 4 return 

def generate_pass():
    length = int(input("Please Enter Password Length: ").strip().lower())
    isupper = input("UpperCase ?(yes/no)").strip().lower()
    isdigit = input("Digit ? (yes/no)")
    isspecial = input("Special Characters? (yes/no)")

    if length < 4:
        print("Password Length must be more than 4 Characters ")
        return
    
    lower = string.ascii_lowercase

    if isupper == "yes":
        upper = string.ascii_uppercase
    else:
        upper = ""

    if isdigit == "yes":
        digit = string.digits
    else:
        digit = ""
    
    if isspecial == "yes":
        special = string.punctuation
    else:
        special = ""
    
    total = lower + upper + digit + special

    print(total)

    




generate_pass()