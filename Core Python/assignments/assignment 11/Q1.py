#  Python Program to Put Even and Odd elements of a List into two Different Lists

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li2 = []
li3 = []

for i in li:
    if(i % 2 == 0):
        li2 = li2 + [i]
    else:
        li3 = li3 + [i]
        
        
print('even numbers:',li2)
print('odd numbers:',li3)