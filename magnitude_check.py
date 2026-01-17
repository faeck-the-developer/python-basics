num1 = int(input("Please type in a number: "))

if num1 < 1000 and num1 > 100:
    print("This number is smaller than 1000")
    print("Thank you!")

if num1 < 100 and num1 < 1000 and num1 > 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")

if num1 < 10 and num1 < 100 and num1 < 1000:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")

if num1 >= 1000:
    print("Thank you!")
