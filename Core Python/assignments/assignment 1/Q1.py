# take input for 5 subjects
sub1 = int(input('Enters marks of subject 1:'))
sub2 = int(input('Enters marks of subject 2:'))
sub3 = int(input('Enters marks of subject 3:'))
sub4 = int(input('Enters marks of subject 4:'))
sub5 = int(input('Enters marks of subject 5:'))

# calculate percentage
sum = sub1+sub2+sub3+sub4+sub5
percentage = (sum/500)*100

#display result
print('percentage :',percentage)
