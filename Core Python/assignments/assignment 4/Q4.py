# print factorial of a number . 

n = int(input('Enter n:'))

fac = 1
for i in range(1, n+1):
    fac = fac * i

print(fac)