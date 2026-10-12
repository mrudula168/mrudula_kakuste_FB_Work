# Fibonacci series : 1 1 2 3 5 8 n terms

def fibonacciSeries(n):
    a = -1
    b = 1
    for i in range(1, n+1):
        c = a+b
        print(c, end = ' ')
        a = b
        b = c
n = int(input('Enter n:'))
fibonacciSeries(n)