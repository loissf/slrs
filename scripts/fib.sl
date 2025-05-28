var start = time()

function fib(n) {
    if n < 1 {
        return 1
    } else {
        return fib(n-1) + fib(n-2)
    }
}

for i, 30 {
    print(i + " " + fib(i))
}

var end = time()
print((end - start) + "ms")