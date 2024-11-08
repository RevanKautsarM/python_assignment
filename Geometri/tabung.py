# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 1-11-2024
# PROJECT100

print('='*40)
print('           KALOR ES')
print('='*40)

m = float(input('Masukan Massa Es\t: '))
l = float(input('Masukan Angka\t: '))
q2 = m*l
print('Kalor Lebur Es\t: ', q2)
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
