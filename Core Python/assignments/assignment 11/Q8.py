# Print 1 to 100 in snakes and ladder pattern.

li = []

for i in range(1, 101):
    li = li + [i]
    
for i in range(0, 100, 10):
    if(i % 20 == 0):
        for j in range(i, i + 10):
            print(li[j], end = ' ')
    else:
        for j in range(i+9, i-1, -1):
            print(li[j], end = ' ')
    print()