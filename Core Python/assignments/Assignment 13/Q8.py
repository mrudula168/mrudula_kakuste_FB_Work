# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

s = input('Enter string:')
d = {}
word = ''

for ch in s:
    if ch != ' ':
        word = word + ch
    else:
        if word != '':
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
                
            word = ''
if word != '':
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(d)