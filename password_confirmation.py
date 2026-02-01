passw = input("Password: ")

while True:
    passinc = input("Repeat password: ")
    
    if passinc == passw:
        print("User account created!")
        break
    else:
        # We use 'else' here because if it's not the same, it MUST be different
        print("They do not match!")
