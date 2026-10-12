# Python Program to Find the Intersection of Two Lists

li = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]
li3 = []

for i in range(len(li)):
    for j in range(len(li2)):
        if(li[i] == li2[j]):
            li3 = li3 + [li[i]]
            # break
            
print(li3)
    