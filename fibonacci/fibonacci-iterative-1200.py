def fib(a):
    x = 0
    y = 1
    for i in xrange(0,a):
        tmp = x + y
        y = x
        x = tmp
    return x

print fib(1200)
