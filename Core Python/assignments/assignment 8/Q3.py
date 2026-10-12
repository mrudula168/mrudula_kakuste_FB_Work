# sum of following series
#a. 1+ 2 + 3 + 4+….. + n

# def sum():
#     sum = 0
#     n = int(input('Enter n:'))
#     for i in range(1, n+1):
#         sum = sum + i
#     print('Sum:', sum)
    
# sum()

#b. 1!+ 2! + 3! + 4!+….. + n!

# def sum():
#     sum = 0
#     fact = 1
#     n = int(input('Enter n:'))
#     for i in range(1, n+1):
#         fact = fact*i
#         sum = sum + fact
#     print('Sum:', sum)

# sum()

#c. 1^1 + 2^2 + 3^3+ …… n^n
def sum():
    sum = 0
    n = int(input('Enter n:'))
    for i in range(1, n+1):
        sum = sum + i**i
    print('Sum:', sum)

sum()