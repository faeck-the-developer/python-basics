limit = int(input("Limit: "))
output = 1
layer = 1
calculation = "1"
while output < limit:
    layer += 1    
    output += layer

    calculation += f" + { layer}"

print (f"The consecutive sum: {calculation} = {output}")
