# strong number

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 145, 146, 40585]

def strongNumber(num):
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1, d + 1):
            fact = fact*i
        sum = sum + fact
    if(num == sum):
        return True
    
res = tuple(filter(strongNumber, data))
print(res)