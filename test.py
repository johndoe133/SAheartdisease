import numpy as np
import sys

sys.setrecursionlimit(1500)

#[0, 1, -1, -1, -1]
def f(n):
    n = n+1
    fib = [0, 1] 
    for i in range(n-2):
        fib += [-1]
    return fibonacci(n, fib)[0:-1]

def fibonacci(n, fib):
    index = n-1
    if fib[index] != -1:
        return fib
    elif fib[index-1] != -1 and fib[index-2] != -1:
        fib[index] = fib[index-1] + fib[index-2]
        return fib
    else:
        #print(fib)
        fib = fibonacci(n-1, fib)
        #print(fib)
        return fibonacci(n-1, fib)

print(f(1000))