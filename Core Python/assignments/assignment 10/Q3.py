# Write a program to find the second largest element in the list.

li = [70, 40, 60, 10, 90]

max = li[0]
smax = 0
for ind in range(1, len(li)):
    if(li[ind] > max):
        smax = max
        max = li[ind]
        
    elif(li[ind] > smax):
        smax = li[ind]
        
print('Second maximum :', smax)