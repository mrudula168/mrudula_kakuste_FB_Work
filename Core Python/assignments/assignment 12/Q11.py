#  Python Program to replace every blank space with hyphen in a string.

str = input('Enter string:')
str2 = ''
for i in str:
    if(i == ' '):
        str2 = str2 + '-'
    else:
        str2 = str2 + i
        
print(str2)