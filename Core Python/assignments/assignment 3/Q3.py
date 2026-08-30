# input angles of triangke to check triangle is valid or not

a = int(input('Enter angle 1 of triangle:'))
b = int(input('Enter angle 2 of triangle:'))
c = int(input('Enter angle 3 of triangle:'))

angle = a + b + c 
if(angle == 180 ):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')