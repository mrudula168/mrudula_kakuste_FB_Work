# prime number
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def primeNumber(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    else:
        return True
            
res = tuple(filter(primeNumber, data))

print(res)