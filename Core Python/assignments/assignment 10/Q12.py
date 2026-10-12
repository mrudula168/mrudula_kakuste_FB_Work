# Write a program to create three lists of numbers, their squares and cubes

li = [1, 2, 3, 4, 5, 6]
li2 = []
li3 = []

for i in li:
    square = i**2
    li2 = li2 + [square]
    cube = i**3
    li3 = li3 + [cube]
    
print('Number:', li)
print('Square:', li2)
print('Cube:', li3)