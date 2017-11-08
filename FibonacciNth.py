# Find the value of the nth in the fibonacci sequence

# DOESN"T WORK
def fib(n):
    if n in [0, 1]:
        return n
    return (fib(n-1)) + (fib(n-2))


fib(7)