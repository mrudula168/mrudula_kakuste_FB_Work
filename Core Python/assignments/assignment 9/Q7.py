# find sum of digits using recursion.

def sum(num):
    if num == 0:
        return 0
    return num % 10 + sum(num // 10)

num = int(input('Enter number:'))
res = sum(num)
print('Sum:', res)