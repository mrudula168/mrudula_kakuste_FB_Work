#1. {} , key & value pair
di = {'Name':'Abhishek', 'Add':'Pune', 3:3.14, 5:3.14, 'Name':'ABC'}

#2. Heterogeneous

#3.Ordered

#4. Key:Immutable, Value:Mutable, Size:Mutable
di['Add'] = 'Mumbai'      #key exist : value update
di[4] = 70                #key doesn't exist : added as a element
print(di)