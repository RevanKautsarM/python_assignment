# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 1-11-2024
# PROJECT100

import os
os.system('cls')
print('='*40)
print('             PROGRAM TABUNG')
print('='*40)
PHI = 22/7
r = float(input('Masukan Jari Jari\t: '))
t = float(input('Masukan Tinggi\t\t: '))
lp = PHI * r**2 + 2 * PHI * r * t
print(f'Luas Permukaan Adalah\t:{lp:.2f}')
