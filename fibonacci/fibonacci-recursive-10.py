def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a-1) + fib(a-2)

print fib(10)
