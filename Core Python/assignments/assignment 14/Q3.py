# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set data type.

li = ['aaple mango', 'banana apple', 'mango apple banana']

s = set()

for string in li:
    words = string.split()
    
    for word in words:
        s.add(word)

d = {}
 
for word in s:
    count = 0
    for string in li:
        words = string.split()
        
        for w in words:
            if word == w:
                count += 1
    d[word] = count

print('Unique words:',s)
print('Frequency:', d)