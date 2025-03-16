import random
import string

def generate_pass():
    length = int(input("Please Enter Password Length: ").strip())
    islower = input("LowerCase ? (yes/no)").strip().lower()
    isupper = input("UpperCase ?(yes/no)").strip().lower()
    isdigit = input("Digit ? (yes/no)").strip().lower()
    isspecial = input("Special Characters? (yes/no)").strip().lower()

    if length < 4:
        print("Password Length must be more than 4 Characters ")
        return
    
    passlist = []

    if islower == "yes":
        lower = string.ascii_lowercase
        passlist.append(random.choice(lower))
    else:
        lower = ""

    if isupper == "yes":
        upper = string.ascii_uppercase
        passlist.append(random.choice(upper))
    else:
        upper = ""

    if isdigit == "yes":
        digit = string.digits
        passlist.append(random.choice(digit))
    else:
        digit = ""
    
    if isspecial == "yes":
        special = string.punctuation
        passlist.append(random.choice(special))
    else:
        special = ""
    
    total = lower + upper + digit + special
    remaining = length - len(passlist)
    password = passlist
    
    for _ in range(remaining):
        character = random.choice(total)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_pass()
print(password)
