# Python Program to Remove the nth Index Character from a Non-Empty String

n = int(input('Enter n:'))
str = 'assignment 12'
str2 = ''

for i in range(len(str)):
    if(i != n):
        str2 = str2 + str[i]

print(str2)