string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# 1. Find the first occurrence
word = string.find(substring)

# If the first occurrence exists...
if word != -1:
    choplen = word + len(substring)
    newstring = string[choplen:]
    
    # 2. Look for the second occurrence ONLY inside this block
    newnum = newstring.find(substring)
    
    if newnum != -1:
        index = newnum + choplen
        print(f"The second occurrence of the substring is at index {index}.")
    else:
        # Found it once, but not twice
        print("The substring does not occur twice in the string.")

else:
    # Didn't even find it once
    print("The substring does not occur twice in the string.")
