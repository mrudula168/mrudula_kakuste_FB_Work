# Write a program to find maximum and minimum element in a list.

li = [5, 40, 60, 10, 90]

max = li[0]
min = li[1]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]
for ind in range(0, len(li)):
    if(li[ind] < min):
        min = li[ind]
print('Maximum :', max)
print('Minimum :', min)