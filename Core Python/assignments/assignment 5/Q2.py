# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. 
# Display all percentage and average percentage of students


n = int(input('Enter number of students:'))

total_percentage = 0
for i in range(1, n + 1):
    print("Student", i)
    sum = 0
    for m in range(5):
        sub = int(input(f'Enter marks of subject {m} :'))
    # sub1 = int(input('Enter marks of subject 1:'))
    # sub2 = int(input('Enter marks of subject 2:'))
    # sub3 = int(input('Enter marks of subject 3:'))
    # sub4 = int(input('Enter marks of subject 4:'))
    # sub5 = int(input('Enter marks of subject 5:'))
        sum = sum + sub
    percentage = (sum/500)*100
    total_percentage = total_percentage + percentage
    print(f'{percentage} percentage of {i} student.')
    
average = total_percentage/n

print('Average percentage of students:', average)
