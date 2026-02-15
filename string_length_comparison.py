word = input ("Please type in string 1: ")
words = input ("Please type in string 2: ")

if len(word) > len(words):

    print (f"{word} is longer")

if len(words) > len(word):
    print (f"{words} is longer")

elif len(words) == len(word):
    print ("The strings are equally long")
