# Write a program of having n number of elements in the list and find out even and odd elements in that list and 
# then create two separate lists which will have even elements and other will have odd elements.

li = [12, 13, 15, 17, 21, 22, 28, 29, 30]
li2 = []
li3 = []

for i in li:
    if( i % 2 == 0):
        li2 = li2 + [i]
    else:
        li3 = li3 + [i]

print('List containing even elements', li2)
print('List containing odd elements', li3)