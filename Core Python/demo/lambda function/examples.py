# area of rectangle
# area = lambda length, breadth : length * breadth
# print(area(10, 20))


# calculating cube
# cube = lambda num : num**3
# print(cube(5))

# calculating square
# square = lambda num : num ** 2
# print(square(7))

# simple interest
# SI = lambda p, r, t : p*r*t/100
# print(SI(10000, 2, 5))

#reverse 3 digit number
rev_num = lambda num : (num//100)*1 + ((num%100)-(num%10)) + (num%10)*100 
print(rev_num(758))