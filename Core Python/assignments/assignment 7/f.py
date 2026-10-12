for i in range(1, 6):
    k = i
    for j in range(1, 7 - i):
        if(i == 1 or j == 1 or i + j == 6 ):
            print(k, end = ' ')
        else:
            print(' ', end = ' ')
        k += 1
    print()