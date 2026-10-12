# Python Program to Remove the Given Key from a Dictionary

key = input('Enter key:')
dict = {'a':1, 'b':2,"c":3}
dict2 = {}

if key in dict:
    for k in dict:
        if k != key:
            dict2[k] = dict[k]
        
    print(dict2)
else:
    print('Key noy found.')