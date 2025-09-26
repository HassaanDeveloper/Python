def sum(s):
    if(s==1):
        return 1
    return sum(s-1) + s

print(sum(5))

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


print(factorial(5))