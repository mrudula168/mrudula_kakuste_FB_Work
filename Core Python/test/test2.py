#1.Write a program to accept year from user and check if it is a leap year or not.

# year = int(input('Enter year:'))

# if(year % 4 ==0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print('Leap year.')
#         else:
#             print('Not a leap year.')
#     else:
#         print('Leap year.')
# else:
#     print('Not a leap year.')
        


#2. Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#Eg : - 428 , 214 etc

# num = int(input('Enter number:'))

# d3 = num % 10
# num = num // 10
# d2 = num % 10
# num = num // 10
# d1 = num % 10
# num = num // 10

# if(d1 == 2*d2 and d1 == d3/2):
#     print('Yes, you have done it.')
    
    
#3.A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. 
# Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. 
# If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

# r = 20
# l = 50
# b = 40
# cost = 35
# # 5 times

# perimeter = (3.14*r + l+l+b)*5
# total_cost = perimeter*35
# print('Total cost :', total_cost)


# 4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

# area = int(input('Enter area of 1 wall:'))
# cost = int(input('Enter cost of painting of 1 wall:'))
# areaof4walls = area*4
# total_cost = areaof4walls * cost
# print('Total cost:', total_cost)


# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

price1 = int(input('Enter price of product:'))
price2 = int(input('Enter price of product:'))
price3 = int(input('Enter price of product:'))
price4 = int(input('Enter price of product:'))
price5 = int(input('Enter price of product:'))

bill = price1 + price2 + price3 + price4 + price5
total_bill = bill + (bill*18/100)
print('Total bill:', total_bill)