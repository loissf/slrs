from time import time

a = "Hello World"
b = "I have something to tell you"

print(a + b)

def baseline(n):
    start = time()
    for i in range(n):
        pass
    return time()-start

c = ""

n = 5000000

base = baseline(n)

print("Empty: ", (base * 1000).__floor__(), " ms")

while True:

    start = time()

    for i in range(n):
        c = a + b

    print( ((time() - start - base) * 1000).__floor__(), " ms" )