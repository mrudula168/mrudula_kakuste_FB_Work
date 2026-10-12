# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = int(input('Enter sum:'))

for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(i+2, len(li)):
            if(li[i] + li[j] + li[k] == sum):
                print('Combinations of 3 numbers are:')
                print(li[i], li[j], li[k])
print('Targer number:', sum)
                
    