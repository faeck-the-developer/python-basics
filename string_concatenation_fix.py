# EXERCISE: Fix the broken code to join three inputs with dashes and an exclamation mark.

# The Problem: The original code used the same variable name for all inputs, 
# overwriting the data each time.

part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")

# The Fix: Using separate variables and 'glueing' them with dashes
print(part1 + "-" + part2 + "-" + part3 + "!")
