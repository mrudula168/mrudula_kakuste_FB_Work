# Python Program to Detect if Two Strings are Anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    count = 0

    for ch in s1:
        if ch in s2:
            count += 1

    if count == len(s1):
        print("Anagram")
    else:
        print("Not Anagram")