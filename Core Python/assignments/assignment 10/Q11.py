# Write a program to print all numbers which are divisible by m and n in the list.

m = int(input('Enter m:'))
n = int(input('Enter n:'))

li = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
li2 = []
for i in li:
    if(i % m == 0 and i % n == 0):
        li2 = li2 + [i]
        
print(f'Numbers divisible by {m} and {n} are: {li2}')