# WAP to print Armstrong number within a given range

range_start = int(input('Enter starting of range:'))
range_end = int(input('Enter ending of range:'))
for i in range(range_start, range_end):
    temp = i
    count = 0
    while(temp > 0):
        count +=1
        temp = temp // 10
    temp = i
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)
    if(sum == i):
        print(i)