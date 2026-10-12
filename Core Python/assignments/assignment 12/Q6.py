# Python Program to Take in a String and Replace Every Blank Space with Hyphen

str = input('Enter string:')
str2 = ''
for i in str:
    if(i == ' '):
        str2 = str2 + '-'
    else:
        str2 = str2 + i
        
print(str2)