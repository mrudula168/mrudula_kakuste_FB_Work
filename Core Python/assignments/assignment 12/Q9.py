# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

# str = 'today is tuesday'
str = 'Python Program to Calculate the Number of Words and the Number of Characters Present in a String'

count = 0
space = 0
for i in str:
    count += 1
    if(i == ' '):
        space += 1
    

print('Characters present in string:', count)
print('words present in string:', space+1)