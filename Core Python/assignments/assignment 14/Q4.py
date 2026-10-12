# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = int(input('Enter sum:'))

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if(li[i] + li[j] == sum):
            print(li[i], li[j])