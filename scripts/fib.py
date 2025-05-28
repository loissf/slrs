from time import time

start = time()

def fib(n):
    res = 0
    if n < 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)

    return res

for i in range(30):
    print(i, fib(i))

end = time()
print((end - start) * 1000, "ms")