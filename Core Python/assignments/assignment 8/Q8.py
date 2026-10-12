# find reverse of a number

def reverseNum(num):
    rev_num = 0
    while(num > 0):
        d = num % 10
        num = num // 10
        rev_num = rev_num*10 + d
    return rev_num
num = int(input('Enter number:'))
res = reverseNum(num)
print(res)