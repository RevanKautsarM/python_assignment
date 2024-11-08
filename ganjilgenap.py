# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

import os
os.system('cls')
print('='*40)
print('             GANJIL GENAP')
print('='*40)

angka = int(input('Masukan Angka\t: '))
for i in range(angka):
    if i % 2 !=0:
        print(f'Angka Ganjil\t= {len(i)}')