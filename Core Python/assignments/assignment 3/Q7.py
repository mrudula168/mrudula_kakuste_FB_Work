# to check if user has entered correct user id and password

userid = input('Enter User id:')
password = input('Enter Password:')

if(userid == 'abcd' and password == '1234' ):
    print('Correct userid and password.')
else:
    print('Wrong userid and password.')
    