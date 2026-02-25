word = input ("Please type in a string: ")

counter = len(word)
second = len(word) - 1

while second > -1:
    
    print (word[second:counter])

    second -= 1
