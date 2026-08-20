# feet and inches into meter and centimeter
# input

print('Enter distant in feet and inches')
feet = int(input('Feet:'))
inches = int(input('Inches:'))

# conversion

inches = feet *12 + inches
cm = inches *2.54
m = cm/100


print('Meter:',m)
print('Centimeter:',cm)