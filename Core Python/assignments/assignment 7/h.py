m = 7
for i in range(1, 6):
    k = 1
    for j in range(1, i + 1):
        print(k, end = ' ')
        k += 1
    for j in range(1, m+1):
        print(' ', end = ' ')
    m -=  2
    k = i
    for j in range(1, i+1):
        if i == 5 and j == 5:
            continue
        elif(i == 5):
            print(k-1, end = ' ')
        else:
            print(k, end = ' ')
        k -=1 
    print()