year = int(input("Year: "))
newyear = year + 1

while True:
    # This logic says: (Divisible by 4 AND not 100) OR (Divisible by 400)
    if (newyear % 4 == 0 and newyear % 100 != 0) or (newyear % 400 == 0):
        print(f"The next leap year after {year} is {newyear}")
        break  # We found it! Exit the loop.
    
    # If we didn't find it, move to the next year and loop again
    newyear += 1
