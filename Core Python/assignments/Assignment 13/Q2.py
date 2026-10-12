# Python Program to Concatenate Two Dictionaries Into One

dict = {'1':'a', '2':'b'}
dict2 = {'3':'c', '4':'d'}
dict3 = {}

for i in dict:
    dict3[i] = dict[i]
for i in dict2:
    dict3[i] = dict2[i]
    
print(dict3)