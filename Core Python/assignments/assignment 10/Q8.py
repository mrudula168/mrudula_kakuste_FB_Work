# Write a program to create a duplicate of an existing list. It should not point to same list.

li1 = [10, 20, 30, 40]

li2 = []

for i in li1:
    li2 = li2 + [i]

print(li2)