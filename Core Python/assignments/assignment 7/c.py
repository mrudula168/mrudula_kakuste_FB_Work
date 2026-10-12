for i in range(1, 6):
    k = 1
    for j in range(1, i + 1):
        if(j == 1 or i == j or i == 5):
            print(k, end = ' ')
        else:
            print(' ', end = ' ')
        k += 1
    print()