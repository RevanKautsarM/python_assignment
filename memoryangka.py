import random
import time

angka = random.randint(100, 999)
print("Ingat angka ini:", angka)
time.sleep(3)

print("\n" * 20)
jawab = input("Masukkan angka: ")

if jawab == str(angka):
    print("Benar")
else:
    print("Salah")