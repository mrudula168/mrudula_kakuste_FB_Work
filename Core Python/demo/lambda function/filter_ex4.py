# armstrong number

data = [153, 154, 155, 370, 371, 372, 1634, 1635, 9474, 9475, 9476]

def armstrongNumber(num):
    temp = num
    count = 0
    while(temp > 0):
        count += 1
        temp = temp // 10
    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d**count)
    if(sum == num):
        return True
    else:
        return False
    
res= tuple(filter(armstrongNumber, data))
print(res)
