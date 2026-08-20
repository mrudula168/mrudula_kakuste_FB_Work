# take input
divisor = int(input('Enter divisor:'))
dividend = int(input('Enter dividend:'))

# calculate quotient and remainder
# for quotient - floor division //
# for remainder - modulus %

quotient = dividend//divisor
remainder = dividend%divisor 

# display result
print('Quotient:',quotient)
print('Remainder:',remainder)