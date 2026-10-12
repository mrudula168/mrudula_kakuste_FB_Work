# check if entered year is a leap year or not.

def leapYear(year):
    if(year % 4 == 0):
        print('Entered year is leap year.')
    else:
        print('Entered year is not leap year.')
year = int(input('Enter year:'))
leapYear(year)