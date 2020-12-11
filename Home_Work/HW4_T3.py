"""def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)"""

"""fib1 = fib2 = 1

n = int(input("Input number Fibonacci: ")) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print(fib2) """
########################################
def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur