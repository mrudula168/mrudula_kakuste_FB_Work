# Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = [ 12, 31, 44, 18, 20, 19]


max = li[0]
smax = 0
size = len(li)
for i in range(1, size):
    for j in range(0, size-1):
        if(li[j] > li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]
            
print('Second largest number:', li[-2])