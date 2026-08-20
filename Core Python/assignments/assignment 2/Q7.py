# sum of three digit number

# input
num = int(input('Enter three digit number:'))

# digit seperation 
d1 = num % 10  # 8
num = num // 10  # 57

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

# addition
sum = d1+d2+d3

# display result
print('Sum of three digit number:',sum)