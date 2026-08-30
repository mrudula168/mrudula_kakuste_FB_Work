# Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. 
# Let him try 3 times. After that program to terminate. 


for i in range(3):
    userid = input('Enter User id:')
    password = input('Enter Password:')
    if(userid == 'abcd' and password == '1234' ):
        print('Correct userid and password.')
        break
    else:   
        print('Wrong userid and password.')
else:
    print('Session terminated')