# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

num = int(input('Enter number:'))

li = [10, 20, 30, 40, 50 , 20]

count = 0

for i in li:
    if(i == num):
        count +=1
    
if(count > 0):
    print(f'Element is present in list, {count} times.')  
else:
    print('Element is not present in list.')