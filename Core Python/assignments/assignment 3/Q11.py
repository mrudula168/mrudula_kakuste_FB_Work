# ticket

total = 0

age1 = int(input('Enter age of person 1:')) 
amount = int(input('Enter amount of ticket:')) 
if(age1 < 12):
    amount = amount - (amount * 30 / 100)
elif(age1 > 59):
    amount = amount - (amount * 50 / 100)
else:
    amount = amount
total = total + amount

age2 = int(input('Enter age of person 2:')) 
amount = int(input('Enter amount of ticket:')) 
if(age2 < 12):
    amount = amount - (amount * 30 / 100)
elif(age2 > 59):
    amount = amount - (amount * 50 / 100)
else:
    amount = amount
total = total + amount

age3 = int(input('Enter age of person 3:')) 
amount = int(input('Enter amount of ticket:')) 
if(age3 < 12):
    amount = amount - (amount * 30 / 100)
elif(age3 > 59):
    amount = amount - (amount * 50 / 100)
else:
    amount = amount
total = total + amount

age4 = int(input('Enter age of person 4:')) 
amount = int(input('Enter amount of ticket:')) 
if(age4 < 12):
    amount = amount - (amount * 30 / 100)
elif(age4 > 59):
    amount = amount - (amount * 50 / 100)
else:
    amount = amount
total = total + amount

age5 = int(input('Enter age of person 5:')) 
amount = int(input('Enter amount of ticket:')) 

if(age5 < 12):
    amount = amount - (amount * 30 / 100)
elif(age5 > 59):
    amount = amount - (amount * 50 / 100)
else:
    amount = amount
total = total + amount

print("Total ticket amount =", total)