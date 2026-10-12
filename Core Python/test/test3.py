# 1. Write a program to print first n prime numbers

# n = int(input('Enter n: '))
# count = 0
# num = 2
# while(count<n):
#     for i in range(2, num):
#         if(num % i == 0):
#             break
#     else:
#         print(num)
#         count +=1
#     num +=1
    
# 2. Write a program to calculate the sum of following series where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

# n = int(input('Enter n:'))
# sum =0
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
#     sum = sum + i/fact
    
# print('Sum:', sum)


#3. Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.

# n = int(input('Enter n:'))
# total_salary = 0
# for i in range(1, n+1):
#     basic_salary = int(input('Enter basic salary:'))

#     if(basic_salary < 20000):
#         da = basic_salary *10/100
#         ta = basic_salary *12/100
#         hra = basic_salary *15/100
#     else:
#         da = basic_salary *15/100
#         ta = basic_salary *18/100
#         hra = basic_salary *20/100
#     salary = basic_salary + da + ta + hra
#     print(f'Total salary of employee{i} : {salary}')
    
#     total_salary = total_salary + salary
# print('Total salary of employees:', total_salary)


#4. Write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101

for i in range(1, 6):
    for j in range(1, 6):
        if((i + j) % 2 == 0):
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()