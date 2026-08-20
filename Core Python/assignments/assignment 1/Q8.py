# convert days into years, weeks, days
#take input

days = int(input('Enter days:'))

# conversion
year = days//365
days = days%365
week = days//7
days = days%7

#display result
print('Years:', year)
print('Weeks:', week)
print('Days:',days)