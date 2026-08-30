# WAP print table of value taken from user

n = int(input('Enter number:'))

i = 1
while(i <= 10):
    s = n*i
    print(f'{n} x {i} = {s}')
    i += 1