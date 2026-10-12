# Python Program to Find the Union of two Lists

li = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]
li3 = []

for i in range(len(li)):
    li3 = li3 + [li[i]]
    
for i in range(len(li2)):
    count = 0
    
    for j in range(len(li3)):
        if(li2[i] == li3[j]):
            count += 1
            break
    if count == 0:
        li3 = li3 + [li2[i]]

print(li3)