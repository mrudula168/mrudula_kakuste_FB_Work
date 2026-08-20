# minimun number of notes needed for representation

amount = int(input('Enter amount:'))

amount1 = amount//2000
amount = amount%2000
print('2000 notes:',amount1)

amount2 = amount//500
amount = amount%500
print('500 notes:',amount2)

amount3 = amount//200
amount = amount%200
print('200 notes:',amount3)

amount4 = amount//100
amount = amount%100
print('100 notes:',amount4)

amount5 = amount//50
amount = amount%50
print('50 notes:',amount5)

amount6 = amount//20
amount = amount%20
print('20 notes:',amount6)

amount7 = amount//10
amount = amount%10
print('10 notes:',amount7)