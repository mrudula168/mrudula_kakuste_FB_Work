# Python Program to Sort the List According to the Second Element in Sublist

li = [[2, 12], [4, 10], [1, 9], [7, 11]]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if(li[i][1] > li[j][1]):
            li[i][1], li[j][1] = li[j][1], li[i][1]
print(li)