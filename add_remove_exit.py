# Part 4: List Addition and Removal Exercise
items = []
counter = 1

while True:
    print(f"The list is now {items}")
    selection = input("a(d)d, (r)emove or e(x)it: ")

    if selection == "x":
        print("Bye!")
        break

    if selection == "d":
        items.append(counter)
        counter += 1
        
    elif selection == "r":
        # Using pop() to remove the last item and syncing the counter
        if len(items) > 0:
            items.pop()
            counter -= 1
