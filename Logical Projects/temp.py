def F_to_C(F):
    return 5*(F-32)/9

F = int(input("Enter temperature in Fahrenhite: "))
a = F_to_C(F)
print(f"{round(a,1)}°C")