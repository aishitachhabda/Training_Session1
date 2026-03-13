w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

s1 = sorted(w1)
s2 = sorted(w2)

if s1 == s2:
    print("Anagram")
else:
    print("Not an Anagram")