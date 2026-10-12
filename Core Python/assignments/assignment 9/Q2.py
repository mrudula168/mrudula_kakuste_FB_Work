# check if given number is Armstrong or not using recursive function.

def countDigit(n):
    if(n ==0):
        return 0
    return 1 + countDigit(n // 10)

def armstrongNum(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrongNum(n // 10, digits)

num = int(input('enter number:'))
digits = countDigit(num)

if(armstrongNum(num, digits) == num):
    print('Armstrong Number.')
else:
    print('Not a Armstrong Number.')