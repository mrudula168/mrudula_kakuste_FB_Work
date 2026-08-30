# calculate profit or loss

sp = int(input('Enter Selling Price:'))
cp = int(input('Enter Cost Price:'))

if(sp > cp):
    print(f'Profit = {sp-cp}.')
else:
    print(f'Loss = {cp-sp}.')
