# li = [10, 20, [30, [40, 50, 60]], 70]

# print(li[2][0])
# print(li[2][1][1])


##HOMEWORK
#WAP to calculate sum of all elements
# li = [[10, 20], [30, 40], [50, 60]]
# sum = li[0][0] + li[0][1] + li[1][0] + li[1][1] + li[2][0] + li[2][1] 
# print(sum)

# sum = 0
# for i in li:
#     for j in i:
#         sum = sum + j
# print(sum)

li = [5, [10, 20], [30, 40], [50, 60]]
# sum = li[0] + li[1][0] + li[1][1] + li[2][0] + li[2][1] + li[3][0] + li[3][1] 
# print(sum)

sum = 5
for i in li[1::]:
    for j in i:
        sum = sum + j
print(sum)
