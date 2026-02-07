print("Please type in integer numbers. Type in 0 to finish.")
attempts = 0
total = 0
positive = 0
negative = 0

while True:
    numbers = int(input("Number: "))
    
    # 1. The Security Guard (Exit Strategy)
    if numbers == 0:
        # Calculate the final mean only once, right before printing
        if attempts > 0:
            mean = total / attempts
        else:
            mean = 0
            
        print(f"Numbers typed in {attempts}")
        print(f"The sum of the numbers is {total}")
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")
        break

    # 2. Sorting (Positives vs Negatives)
    if numbers > 0:
        positive += 1
    elif numbers < 0:
        negative += 1

    # 3. The Gift Bag (Math for valid numbers)
    attempts += 1
    total += numbers
