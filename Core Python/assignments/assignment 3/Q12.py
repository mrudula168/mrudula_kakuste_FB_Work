# check number is palinrome or not

num = int(input('Enter 3 digit number:'))

d1 = num % 10
num = num // 10
d2 = num % 10
num = num // 10
d3 = num % 10
num = num // 10

if(d1 == d3):
    print('Number is palindrome.')
else:
    print('Number is not palindrome.')