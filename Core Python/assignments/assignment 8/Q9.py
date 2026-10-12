#  check if entered number is a palindrome or not.

def pallindrome(num):
    rev_num = 0
    temp = num
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev_num = rev_num*10 + d
    if(rev_num == num):
        print('Number is pallindrome number.')
    else:
        print('Number is not pallindrome number.')
num = int(input('Enter number:'))
pallindrome(num)