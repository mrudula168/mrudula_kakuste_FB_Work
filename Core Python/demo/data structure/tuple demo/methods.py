# tu = (10, 20, 30, 10)

# print(tu.count(10))
# print(tu.index(30))



# add elements in tuple
tu = (10, 20, 30)
li = list(tu)        # convert tuple into list
print(type(li))
li.append(40)        # make changes into list
print(li)
tu = tuple(li)       # convert list into tuple
print(type(tu))
print(tu)