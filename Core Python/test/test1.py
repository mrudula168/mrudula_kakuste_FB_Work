# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:

l = int(input('Enter length:'))
b = int(input('Enter breadth:'))
r = int(input('Enter radius:'))

area = l * b + (3.14* r**2)/2
perimeter = 2*(l+b) + 3.14 * r

print('Area:', area)
print('Perimeter:',perimeter)


#2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100) 

# p = int(input('Enter principal, p:'))
# r = int(input('Enter rate, r:'))
# t = int(input('Enter time, t:'))

# SI = p*r*t/100

# print('Simple Intereset:', SI)


#3. Write a program to accept distance in km and convert it into meters and centimeters both. 

# km = int(input('Enter distance km:'))

# m = km*1000
# cm = km*100000

# print('Distance in m:', m)
# print('Distance in cm:', cm)

#4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall. 

# area = int(input('Enter area or 1 wall:'))
# interior_cost = int(input('Enter cost of interior wall:'))
# exterior_cost = int(input('Enter cost of exterior wall:'))

# interior_total = 3 * area * interior_cost
# exterior_total = 4 * area * exterior_cost

# total = interior_total + exterior_total

# print('Total cost:', total)