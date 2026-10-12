# Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = 'banana'
str2 = ''
for i in str:
    if(i == 'a'):
        str2 = str2 + '$'
    else:
        str2 = str2 + i
print(str2)