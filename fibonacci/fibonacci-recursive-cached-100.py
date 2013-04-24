def memoize(function):
    memo = {}
    def cache(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return cache

@memoize
def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a-1) + fib(a-2)

print fib(100)
