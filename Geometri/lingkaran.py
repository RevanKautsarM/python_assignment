# Dibuat Oleh : Revan
# Tanggal     : 21-10-2024
# Soal Lingkaran/PROJECT100

import os
os.system('cls')
print('='*40)
print('           PROGRAM LINGKARAN')
print('='*40)

PHI = 22/7

def input_user():
    r = float(input('Masukan Jari Jari Lingkaran\t: '))
    return r

luas_lingkaran = lambda r : r ** 2 * PHI
keliling_lingkaran = lambda r : 2 * PHI * r

r = input_user()
print(f'Hasil Perhitungan Luas Lingkaran\t: {luas_lingkaran(r):.2f}')
print(f'Hasil Perhitungan Keliling Lingkaran\t: {keliling_lingkaran(r):.2f}')