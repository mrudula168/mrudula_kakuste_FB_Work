# Calculate simple interest

#take input
P = int(input('Enter Principle Amount:'))
R = int(input('Enter Rate of interest in %:'))
T = int(input('Enter Time in years:'))

# calculate simple interest
SI = (P*R*T)/100

# display result
print('Simple Interest:',SI)