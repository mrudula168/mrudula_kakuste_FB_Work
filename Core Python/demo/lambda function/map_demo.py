#syntax:
#map(function, iterables)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#method 1:
# def square(n):
#     return n * n
# res = list(map(square, data))

#method 2:
res = list(map(lambda n: n * n, data))

print(res)