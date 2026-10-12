# Write a program to remove all occurrences of a given element in the list

n = int(input('Enter element:'))

li = [10, 12, 13, 19, 17, 19, 20]
li2 = []
for i in li:
    if(i != n):
        li2 = li2 + [i]
        
print('Original list',li)
print('List after removing element.', li2)