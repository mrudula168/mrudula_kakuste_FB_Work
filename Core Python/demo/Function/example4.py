# check armstrong number

#Type 1: without passing parameter, without returning value

# def armstrongNumber():
#     num = int(input('Enter number to check it is armstrong or not:'))
#     temp = num
#     count = 0
#     while temp > 0:
#         count += 1
#         temp = temp // 10
#     temp = num
#     sum = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         sum = sum + d**count
#     if(num == sum):
#         print(True)
#     else:
#         print(False)

# armstrongNumber()


#Type 2: with passing parameter, without returning value
# def armstrongNumber(num):
#     temp = num
#     count = 0
#     while temp > 0:
#         count += 1
#         temp = temp // 10
#     temp = num
#     sum = 0
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         sum = sum + d**count
#     if(num ==sum):
#         print(True)
#     else:
#         print(False)
        
# num = int(input('Enter number to check it is armstrong or not:'))
# armstrongNumber(num)


#Type 3: without passing parameter, with returning value
# def armstrongNumber():
#     num = int(input('Enter number to check it is armstrong or not:'))
#     temp = num
#     count = 0
#     while temp > 0:
#         count += 1
#         temp = temp // 10
#     temp = num
#     sum = 0 
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         sum = sum + d**count
#     if(num ==sum):
#         return True
#     else:
#         return False
# res = armstrongNumber()
# print(res)


# Type 4: with passing parameter, with returning value
def armstrongNumber(num):
    temp = num
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        sum = sum + d**count
    if(num == sum):
        return True
    else:
        return False
    
num = int(input('Enter number to check it is armstrong or not:'))
res = armstrongNumber(num)
print(res)