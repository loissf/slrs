from time import time

start = time()

def compt_pi(n):
    k = 1
    s = 0
    sign = 1
    for i in range(n):
        s = s + ( sign * (4.0/k) )
        sign = sign * -1
        k = k + 2

    return s

print(compt_pi(1000000))

end = time()
print((end - start) * 1000, "ms")