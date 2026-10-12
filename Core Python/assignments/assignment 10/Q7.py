#  Write a program to create a new list from existing list which contains cube of each number of list.

li = [1, 2, 3, 4, 5, 6]

li2 = []

for i in li:
    cube = i**3
    li2 = li2 + [cube]

print(li2)