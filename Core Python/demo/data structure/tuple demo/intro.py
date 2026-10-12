#1. ()
# tu = (10,)  #use comma for single value otherwise object class is created
# tu = (10, 20, 30, 'a', 3.14, 10)

#2. Heterogeneous

#3.Ordered

#4. Immutable
# tu[0] = 5    #raise error

#5. Duplicate elements allowed


#6. tuple is faster than list beacuse less in size
li = []
tu = ()
import sys

print(sys.getsizeof(tu))
print(sys.getsizeof(li))

# print(type(tu))
# print(tu)