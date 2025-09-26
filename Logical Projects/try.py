try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print("An error occurred: ", str(e))

print("Thanks!")