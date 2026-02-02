teks = input("Teks: ")
geser = int(input("Geser: "))

hasil = ""

for c in teks:
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        hasil += chr((ord(c) - base - geser) % 26 + base)
    else:
        hasil += c

print(hasil)