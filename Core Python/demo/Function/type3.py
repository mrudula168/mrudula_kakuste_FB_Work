# 2.1.3 without passing parameter, with returning value

def addition():
    num1 = int(input('Enter number 1:'))
    num2 = int(input('Enter number 2:'))
    
    sum = num1 + num2
    
    return sum

res = addition()
print(res)