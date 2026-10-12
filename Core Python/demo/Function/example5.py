# check perfect number

# Type 1: without passing parameter, without returning value
# def perfectNumber():
#     num = int(input('Enter number to check it is perfect or not:'))
#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i
#     if(num == sum):
#         print(True)
#     else:
#         print(False)

# perfectNumber()

#Type 2: with passing parameter, without returning value

# def perfectNumber(num):
#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i
#     if(num == sum):
#         print(True)
#     else:
#         print(False)
# num = int(input('Enter number to check it is perfect or not:'))
# perfectNumber(num)

#Type 3: without passing parameter, with returning value
# def perfectNumber():
#     num = int(input('Enter number to check it is perfect or not:'))
#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i
#     if(num == sum):
#         return True
#     else:
#         return False
# res = perfectNumber()
# print(res)

#Type 4: with passing parameter, with returning value
def perfectNumber(num):
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    if(num == sum):
        return True
    else:
        return False
num = int(input('Enter number to check it is perfect or not:'))
res = perfectNumber(num)
print(res)
