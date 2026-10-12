# check whether a number is prime or not using recursion

def primeNum(num, i=2):
    if num == 0 or num == 1:
        return 0
    if i == num:
        return 1
    if num % i == 0:
        return 0
    
    return primeNum(num, i + 1)

num = int(input('Enter number:'))

if(primeNum(num) == 0):
    print('not a prime number')
else:
    print('prime number')