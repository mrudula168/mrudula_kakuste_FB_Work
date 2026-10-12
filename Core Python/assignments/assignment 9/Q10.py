#  reverse a number using recursion.

def reverse(num, rev = 0):
    if num == 0:
        return rev
    rev = rev*10 + num%10
    return reverse(num//10 , rev)

num = int(input('Enter number:'))
res = reverse(num)
print('Reverse number:', res)