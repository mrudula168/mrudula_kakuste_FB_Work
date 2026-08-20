# area of triangle and rectangle
# input

print('Enter dimensions of triangle:')
b = int(input('Enter Base:'))
h = int(input('Enter Height:'))

print('Enter dimensions of rectangle:')
l = int(input('Enter Length:'))
w = int(input('Enter weight:'))

# calculations

triangle = (b*h)/2
rectangle = l*w

# display result
print('Area of triangle:',triangle)
print('Area of rectangle',rectangle)
