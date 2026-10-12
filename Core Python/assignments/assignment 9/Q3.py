# reverse a given number using recursive function.

def reverseNum(num, rev = 0):
    if num == 0:
        return rev
    return reverseNum(num // 10, rev*10 + num % 10)

num = int(input('enter number:'))
res = reverseNum(num)
print('Reverse number:', res)