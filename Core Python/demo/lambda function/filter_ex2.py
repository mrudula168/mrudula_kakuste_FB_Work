# perfect number
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 29, 496]

def perfectNumber(num):
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    if(num == sum):
        return True
    
res = tuple(filter(perfectNumber, data))
print(res)