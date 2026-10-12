#  print Fibonacci series using recursion

def fibonacci(n, a = -1, b = 1 ):
    if n == 0:
        return 0
    print(a+b, end = ' ') 
    fibonacci(n - 1, a = b, b = a+b)

n = int(input('Enter n:'))
fibonacci(n)