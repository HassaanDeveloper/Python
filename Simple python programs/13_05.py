from functools import reduce
l = [23, 4555, 68685, 9909, 123, 454245]

def greater(a, b):
    if(a > b):
        return a
    return b

print(reduce(greater, l))