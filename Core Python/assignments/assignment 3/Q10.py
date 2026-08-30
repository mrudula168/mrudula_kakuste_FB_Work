# to check if person is eligible to marry or not

gender = input('Enter M for Male or F for Female:')
age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >= 18):
        print('Eligible to marry.')
    else:
        print('Not eligible to marry.')
else:
    if(age>= 21):
        print('Eligible to marry.')
    else:
        print('Not eligible to marry.')