# check palindrome number.

#Type1: without passing parameter, without returning value

# def palindromeNumber():
#     num = int(input('Enter number to check it is palindrome or not:'))
#     temp = num
#     rev_num = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         rev_num = rev_num * 10 + d
#     if(rev_num == num):
#         print(True)
#     else:
#         print(False)
        
# palindromeNumber()


# Type 2: with passing parameter, without returning value
# def pallindromeNumber(num):
#     temp = num
#     rev_num = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         rev_num = rev_num * 10 + d
#     if(rev_num == num):
#         print(True)
#     else:
#         print(False)
        
# num = int(input('Enter number to check it is pallindrome or not:'))
# pallindromeNumber(num)


#Type 3: without passing parameter, with returning value

# def pallindromeNumber():
#     num = int(input('Enter number to check it is pallindrome or not:'))
#     temp = num
#     rev_num = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         rev_num = rev_num * 10 + d
#     if(rev_num == num):
#         return True
#     else:
#         return False
    
# res = pallindromeNumber()
# print(res)


# Type 4: with passing parameter, with returning value

def pallindromeNumber(num):
    temp = num
    rev_num = 0
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        rev_num = rev_num * 10 + d
    if(rev_num == num):
        return True
    else:
        return False
num = int(input('Enter number to check it is pallindrome or not:'))
res = pallindromeNumber(num)
print(res)