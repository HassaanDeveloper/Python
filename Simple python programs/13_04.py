def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [23, 4555, 68685, 9909, 123, 454245]

f = list(filter(divisible5, a))
print(f)