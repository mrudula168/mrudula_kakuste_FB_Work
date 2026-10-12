# find sum of n numbers using recursion.

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

n = int(input('Enter n:'))
res = sum(n)
print('Sum of series:', res)
