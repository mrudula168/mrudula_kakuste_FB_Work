# 

userid = input('Enter User id:')
password = input('Enter Password:')

if(userid == 'abcd' and password == '1234' ):
    print('Correct userid and password.')
    captcha = 5678
    print('Captcha:',captcha)
    code = int(input('Enter Captcha:'))
    if(code == 5678):
        print('Success.')
    else:
        print('Failed')
else:
    print('Wrong userid and password.')
    