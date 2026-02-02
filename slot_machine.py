import random

simbol = ["A", "B", "C"]
hasil = [random.choice(simbol) for _ in range(3)]

print(hasil)

if hasil[0] == hasil[1] == hasil[2]:
    print("Menang!")
else:
    print("Coba lagi")