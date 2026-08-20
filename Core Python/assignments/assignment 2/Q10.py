# reverse three digit number
# input
num = int(input('Enter number:'))

# digit separation     345
a = num // 100         #3
b = (num // 10) % 10   #4
c = num % 10           #5

#reverse
reverse = c * 100 + b * 10 + a

print('Reverse :', reverse)