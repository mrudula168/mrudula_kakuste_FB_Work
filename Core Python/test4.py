# Write a function to which we pass a parameter and print the factors of a given number
# For Eg: Factors of 12 : 1,2,3,4,6,12

# def factors(num):
#     for i in range(1, num+1):
#         if(num % i == 0):
#             print(i, end = ' ')
    
# num = int(input('Enter number:'))
# factors(num)


# Write a program to find factorial of given number using recursion

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
    
# n = int(input('Enter n:'))
# res = fact(n)
# print('Factorial:',res)
    

# WAP to print following patterns : z

def pattern():
    print('*'*22)
    space=22
    for i in range(11):
        print(' '*space+'*')
        space=space-2
    print('*'*21 +'*')
pattern()