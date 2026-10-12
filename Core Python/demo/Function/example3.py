# check strong number

#Type 1: without passing parameter, without returning value
# def strongNumber():
#     num = int(input('Enter number to check it is strong number or not:'))
#     temp = num
#     sum = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         fact = 1
#         for i in range(1, d + 1):
#             fact = fact * i
#         sum = sum + fact
#     if(num == sum):
#         print(True)
#     else:
#         print(False)

# strongNumber()


#Type 2: with passing parameter, without returning value
# def strongNumber(num):
#     temp = num
#     sum = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         fact = 1
#         for i in range(1, d + 1):
#             fact = fact * i
#         sum = sum + fact
#     if(num == sum):
#         print(True)
#     else:
#         print(False)
# num = int(input('Enter number to check it is strong or not:'))
# strongNumber(num)


# Type 3: without passing parameter, with returning value
# def strongNumber():
#     num = int(input('Enter number to check it is strong or not:'))
#     temp = num
#     sum = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         fact = 1
#         for i in range(1, d + 1):
#             fact = fact * i
#         sum = sum + fact
#     if(num == sum):
#         return True
#     else:
#         return False
    
# res = strongNumber()
# print(res)


# Type 4: with passing parameter, with returning value
def strongNumber(num):
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1, d + 1):
            fact = fact * i
        sum = sum + fact
    if(num == sum):
        return True
    else:
        return False
num = int(input('Enter number to check it is strong or not:'))
res = strongNumber(num)
print(res)