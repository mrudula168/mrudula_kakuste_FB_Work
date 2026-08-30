# to check triangle is euilateral isosceles or scalene

a = int(input('Enter side 1 of triangle:'))
b = int(input('Enter side 2 of triangle:'))
c = int(input('Enter side 3 of triangle:'))

if(a == b == c):
    print('Triangle is Equilateral.')
elif(a == b or b == c or a == c):
    print('Triangle is Isosceles.')
else:
    print('Triangle is Scalene.')