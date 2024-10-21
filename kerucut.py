# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 21-10-2024
# Soal Kerucut

import math
import os
os.system('cls')
print('='*40)
print('           PROGRAM KERUCUT')
print('='*40)

PHI = 22/7
sisi_miring = math.sqrt(r**2 + tinggi**2)
LUAS_ALAS = r ** 2 * PHI
LUAS_SELIMUT = r * PHI * sisi_miring

def input_user():
    global r
    global tinggi
    r = float(input('Masukan Nilai Jari Jari\t: '))
    tinggi = float(input('Masukan Nilai Tinggi Kerucut\t: '))
    return r,tinggi
r,tinggi = input_user()

volume_kerucut = lambda r,tinggi : r ** 2 * PHI * 1/3 * tinggi
luas_kerucut = lambda LUAS_ALAS,LUAS_SELIMUT : LUAS_ALAS + LUAS_SELIMUT

print(f'Hasil Perhitungan Volume Kerucut Adalah\t: {volume_kerucut(r,tinggi):.2f}')
print(f'Hasil Perhitungan Luas Kerucut Adalah\t: {luas_kerucut(LUAS_ALAS,LUAS_SELIMUT):.2f}')