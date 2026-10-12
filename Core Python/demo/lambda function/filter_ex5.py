# pallindrome number

data = [10, 11, 12, 13, 120, 121, 123, 222, 313, 333, 345, 400, 414, 456]

def pallindromeNumber(num):
    rev_num = 0
    temp = num
    while temp > 0:
        d = temp % 10
        temp = temp // 10

        rev_num = rev_num*10 + d
    if(num == rev_num):
        return True

res = tuple(filter(pallindromeNumber, data))
print(res)