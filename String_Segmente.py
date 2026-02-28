word = input("Please type in a word: ")
cha = input ("Please type in a character: ")

index = word.find(cha)
second = index + 3

while cha in word and index <= len(word) - 3:

    print (word[index:second])
    word = word[index + 1:]

    index = word.find(cha)
    second = index + 3
