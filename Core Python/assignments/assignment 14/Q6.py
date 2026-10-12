# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = set(li)

max_product = None
num1 = 0
num2 = 0
for i in s:
    for j in s:
        if(i != j):
            product = i * j
            
            if max_product is None or product > max_product :
                max_product = product
                
                num1 = i
                num2 = j
print('Number:', num1, num2)
print('Maximum product:', max_product)