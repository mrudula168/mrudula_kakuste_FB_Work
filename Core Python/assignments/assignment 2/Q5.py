# calculate sp based on cp and discount

#input
cp = int(input('Enter cost price of book:'))
discount = int(input('Enter discount:'))

# calculation
sp = cp - (discount/100)*cp

print('Selling price:',sp)