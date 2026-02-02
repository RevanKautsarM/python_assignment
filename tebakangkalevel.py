import random

level = int(input("Level (1=1-10, 2=1-50, 3=1-100): "))

if level == 1:
    max_angka = 10
elif level == 2:
    max_angka = 50
else:
    max_angka = 100

angka = random.randint(1, max_angka)

while True:
    tebak = int(input("Tebak angka: "))
    if tebak == angka:
        print("Benar")
        break
    elif tebak < angka:
        print("Terlalu kecil")
    else:
        print("Terlalu besar")