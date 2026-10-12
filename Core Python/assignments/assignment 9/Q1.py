#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +….. + n!

def fact(n):
    if n == 0 or n== 1:
        return 1
    return n * fact(n-1)

def sumOfSeries(n):
    if n == 1:
        return 1
    return fact(n) + sumOfSeries(n - 1)
    
n = int(input('Enter n:'))
res = sumOfSeries(n)
print('sum:', res)