# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100
import random

def tebak_angka():
    angka = random.randint(1, 100)
    while True:
        tebak = int(input("Tebak angka (1-100): "))
        if tebak == angka:
            print("Selamat! Anda menang!")
            break
        elif tebak < angka:
            print("Terlalu kecil!")
        else:
            print("Terlalu besar!")

tebak_angka()