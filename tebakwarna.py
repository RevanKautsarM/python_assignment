# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100
import random

def tebak_warna():
    warna = ["Merah", "Hijau", "Biru", "Kuning", "Ungu"]
    warna_acak = random.choice(warna)
    tebak = input("Tebak warna (Merah, Hijau, Biru, Kuning, Ungu): ")
    if tebak.capitalize() == warna_acak:
        print("Selamat! Anda benar!")
    else:
        print(f"Salah! Warna yang benar adalah {warna_acak}.")

tebak_warna()