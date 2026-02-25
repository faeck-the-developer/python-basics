word = input("Word: ")
lol = "*"

# The frame is 30 characters wide. 
# We subtract 2 for the edge stars, leaving 28 for the inside.
spacing = 28 - len(word)
spac = spacing // 2
newspace = spacing - spac

print(lol * 30)
print(f"*{' ' * spac}{word}{' ' * newspace}*")
print(lol * 30)
