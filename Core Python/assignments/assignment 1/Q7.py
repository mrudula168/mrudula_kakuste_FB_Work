# find roots of quadratic equation
# ax^2+bx+c
# take input     
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

# calculate D, root1 and root2
D = b**2 - 4*a*c
root1 = (- b + D**0.5)/(2*a)
root2 = (- b - D**0.5)/(2*a)

#display result
print('Root 1:',root1)
print('Root 2:',root2)