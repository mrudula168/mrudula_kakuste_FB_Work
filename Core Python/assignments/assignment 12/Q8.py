# Python Program to Remove the Characters of Odd Index Values in a String

str = 'python program'
str2 = ''

for i in range(len(str)):
    if(i % 2 != 0):
        continue
    else:
        str2 = str2 + str[i]
        
print(str2)