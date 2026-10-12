# Python Program to count number of digits and letters in a string.

str = input('Enter string:')

countD = 0
countL = 0

for i in str:
    if(i >= '0' and i <= '9'):
        countD += 1
    else:
        countL += 1
print('Number of digits:', countD)
print('Number of letters:', countL)