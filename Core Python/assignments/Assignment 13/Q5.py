# Python Program to Sum All the Items in a Dictionary

dict = {'a':1, 'b':2,"c":3}
sum = 0

for values in dict.values():
    sum = sum + values
print(sum)