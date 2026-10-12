# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

# str = 'python'
str = 'program'
str2 = ''

size = len(str)
for i in range(size):
    if(i == 0):
        str2 = str2 + str[size-1]
    elif(i == size-1):
        str2 = str2 + str[0]
    else:
        str2 = str2 + str[i]
        
print(str2)