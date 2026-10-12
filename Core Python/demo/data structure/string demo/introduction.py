#1. '', " ", ''' ''', """ """
str = 'Firstbit solutions'
str = "Firstbit solutions"
str = '''This is first line.
This is second line.'''
str = """This is first line.
This is second line."""

#2. Set of characters (alpha, digits, symbols, space)

#3. Ordered (to maintain meaning of text)

#4. Immutable (Faster execution)

#5. Duplicate characters are allowed

# print(type(str))


##HOMEWORK
#reverse the string without using slicing

str ='Hello'

rev = ''
for char in str:
    rev = char + rev
print(rev)