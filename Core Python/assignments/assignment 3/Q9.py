# input 5 subject marks from user and display grade

sub1 = int(input('Enter subject 1 marks:'))
sub2 = int(input('Enter subject 2 marks:'))
sub3 = int(input('Enter subject 3 marks:'))
sub4 = int(input('Enter subject 4 marks:'))
sub5 = int(input('Enter subject 5 marks:'))

sum = (sub1 + sub2 + sub3 + sub4 + sub5)/500
percentage = sum*100

if(percentage > 90):
    print('First Class, Percentage:',percentage)
elif(percentage > 80):
    print('Second Class, Percentage:',percentage)
elif(percentage > 70):
    print('Third Class, Percentage:',percentage)
elif(percentage > 60):
    print('Forth Class, Percentage:',percentage)
else:
    print('Fail.')
