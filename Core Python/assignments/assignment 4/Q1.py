# print all even numbers till n

n = int(input('Enter n:'))

for i in range(n+1):
    if(i % 2 == 0):
        print(i)
    