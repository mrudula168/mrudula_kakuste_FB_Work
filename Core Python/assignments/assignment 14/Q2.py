# Write a Python program to remove the intersection of a second set with a first set

s1 = {10, 20, 30, 40, 50, 60}
s2 = {30, 40, 50, 60}

for i in s2:
    if i in s1:
        s1.remove(i)
print(s1)