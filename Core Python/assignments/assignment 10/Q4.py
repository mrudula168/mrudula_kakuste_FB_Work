# Write a program to reverse the list

li = [10, 20, 30, 40, 50]
li2 = []
for ind in range(len(li)-1, -1, -1):
    li2 = li2 + [li[ind]]
print(li2)