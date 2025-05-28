from time import time

def bench(func, n):
    start = time()

    func(n)

    return ((time() - start) * 1000).__floor__()

def calls(n: int):
    def B():
        pass

    class Test:
        def A(self):
            pass

    a = Test()

    for i in range(n):
        B()
        a.A()

def pi(n):
    k = 1
    s = 0
    sign = 1
    for i in range(n):
        s = s + ( sign * (4.0/k) )
        sign = sign * -1
        k = k + 2

    return s


def fib(n):
    res = 0
    if n < 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)

    return res

def concat(n):
    a = "This is a big string"
    b = "This is another big string"
    res = ""
    for i in range(n):
        res = a + b

    return res

baseline = [374, 273, 394, 361]
baseline_total = 374 + 273 + 394 + 361

n = 1000000

while True:
    res_calls  = bench(calls, n * 10)
    res_pi     = bench(pi, n * 4)    
    res_fib    = bench(fib, 32)      
    res_concat = bench(concat, n * 6)

    print("calls   ->  ", res_calls , " ms    ", (100.0 / baseline[0]) * res_calls , "%")
    print("pi      ->  ", res_pi    , " ms    ", (100.0 / baseline[1]) * res_pi    , "%")
    print("fib     ->  ", res_fib   , " ms    ", (100.0 / baseline[2]) * res_fib   , "%")
    print("concat  ->  ", res_concat, " ms    ", (100.0 / baseline[3]) * res_concat, "%")

    total = (res_calls + res_pi + res_fib + res_concat)

    print("total   ->  ", total, " ms   ", (100.0 / baseline_total) * total, "%")

    print("-----------------------------------------")