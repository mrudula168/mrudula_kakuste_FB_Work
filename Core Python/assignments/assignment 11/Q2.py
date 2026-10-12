# Python Program to Merge Two Lists and Sort it

li1 = [1, 13, 15, 6, 19]
li2 = [2, 8, 3, 20, 14]
li3 = []

for i in li1:
    li3 = li3 + [i]
for i in li2:
    li3 = li3 + [i]
    
size = len(li3)
for i in range(1, size):
    for j in range(0, size-1):
        if(li3[j] > li3[j+1]):
            li3[j], li3[j+1] = li3[j+1], li3[j]
            
print(li3)