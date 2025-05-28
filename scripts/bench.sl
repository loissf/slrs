function bench(func, n) {
    var func: Function = func

    var start = time()

    func(n)

    return (time() - start)
}

function calls(n: int) {
    function B() {}

    class Test {
        function A() {}
    }

    var a = Test()

    for i, n {
        B()
        a.A()
    }
}

function pi(n) {
    var k = 1
    var s = 0
    var sign = 1
    for i, n {
        s = s + ( sign * (4.0/k) )
        sign = sign * -1
        k = k + 2
    }
    return s
}

function fib(n) {
    if n < 1 {
        return 1
    } else {
        return fib(n-1) + fib(n-2)
    }
}

function concat(n) {
    var a = "This is a big string"
    var b = "This is another big string"
    var res: string = ""
    for i, n {
        res = a + b
    }
}
var baseline = [374, 273, 394, 361]
var baseline_total = 374 + 273 + 394 + 361

var n = 1000000

for i, 2 {
    var calls  = bench(calls, n * 10)
    var pi     = bench(pi, n * 4)    
    var fib    = bench(fib, 32)      
    var concat = bench(concat, n * 6)

    print("calls   ->  " + calls  + " ms    " + (100.0 / baseline[0]) * calls  + "%")
    print("pi      ->  " + pi     + " ms    " + (100.0 / baseline[1]) * pi     + "%")
    print("fib     ->  " + fib    + " ms    " + (100.0 / baseline[2]) * fib    + "%")
    print("concat  ->  " + concat + " ms    " + (100.0 / baseline[3]) * concat + "%")

    var total = (calls + pi + fib + concat)

    print("total   ->  " + total + " ms   " + (100.0 / baseline_total) * total + "%")

    print("-----------------------------------------")
}