# Write a program to remove duplicates from the list.

li = [10, 20, 30, 40, 50, 20, 50]

li2 = []

for i in li:
    count = 0
    for j in li2:
        if i == j:
            count += 1
            
    if(count == 0):
        
        li2 = li2 + [i]
        
print('Original list', li)
print('List after removing duplicate values', li2)