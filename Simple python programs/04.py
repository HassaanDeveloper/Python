try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    d = a/b
    print(d)
except ZeroDivisionError as e:
    print("Infinite")