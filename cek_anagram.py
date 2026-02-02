a = input("Kata 1: ").replace(" ", "").lower()
b = input("Kata 2: ").replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Bukan anagram")
