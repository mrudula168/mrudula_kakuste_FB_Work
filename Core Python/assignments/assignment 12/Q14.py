# Python Program to count the occurrences of ach word in a string.

str = input('Enter string:')

count = 0

for i in str:
    if(i == 'ach'):
        count += 1
print('Occurences of ach in string:', count)