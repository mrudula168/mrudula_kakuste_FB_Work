# check prime number

# type 1: without passing parameters, without returning value
# def primeNumber():
#     num = int(input('Enter number to check it is prime or not:'))

#     for i in range(2, num):
#         if(num % i == 0):
#             print(False)
#             break
#     else:
#         print(True)

# primeNumber()

# type 2: with passing parameter, without returning value
# def primeNumber(num):
#     for i in range(2, num):
#         if(num % i == 0):
#             print(False)
#             break
#     else:
#         print(True)
        
# num = int(input('Enter number to check it is prime or not.'))
# primeNumber(num)


# Type 3: without passing parameter, with returning value

# def primeNumber():
#     num = int(input('Enter number to check it is prime or not:'))
    
#     for i in range(2, num):
#         if(num % i == 0):
#             return False
#             break
#     else:
#         return True

# res = primeNumber()
# print(res)

# Type 4: with passing parameter, with returning value

def primeNumber(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
            break
    else:
        return True
    
num = int(input('Enter number to check it is prime or not:'))

res = primeNumber(num)
print(res)
    