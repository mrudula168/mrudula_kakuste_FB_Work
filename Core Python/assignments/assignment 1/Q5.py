# calculate compound interest

#take input
P = int(input('Enter Principle Amount:'))
R = int(input('Enter Rate of interest in %:'))
T = int(input('Enter Time in years:'))

# calculate compound interest
CI = P*(1+R/100)**T-P

#display result
print('Compound Interest:',CI)