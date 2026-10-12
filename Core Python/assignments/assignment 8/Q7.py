# find sum of digits of a number.

def sum(n):
    sum = 0
    while(n>0):
        d = n % 10
        n = n // 10
        sum = sum + d
    print(sum)
n = int(input('Enter 3 digit number:'))
sum(n)