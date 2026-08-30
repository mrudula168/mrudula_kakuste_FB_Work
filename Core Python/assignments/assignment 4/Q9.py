# print all numbers in a range divisible by a given number. 

range_start = int(input('Enter starting of range:'))
range_end = int(input('Enter ending of range:'))
num = int(input('Enter number:'))

for i in range(range_start, range_end + 1):
    if(i % num == 0):
        print(i)