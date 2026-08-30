# check triangle is valid or not by sides

a = int(input('Enter side 1 of triangle:'))
b = int(input('Enter side 2 of triangle:'))
c = int(input('Enter side 3 of triangle:'))

if( a + b > c and a + c > b and b + c > a):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')