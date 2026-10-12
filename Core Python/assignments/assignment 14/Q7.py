# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa.
# Use the Python set.

s1 = {10, 20, 30, 40, 50, 60}
s2 = {30, 40, 50, 60, 70, 80}

print('Elements in first set but not in second', s1 - s2)
print('Elements in second set but not in first', s2 - s1)