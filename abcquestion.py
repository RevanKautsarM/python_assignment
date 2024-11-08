# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

import os
os.system('cls')
print('='*40)
print('               Pertanyaan ABC')
print('='*40)

pertanyaan = print("""Berapa hasil dari 100 * 0?
    A. 0
    B. 1000
    C. 100""")
print('A. 0 B. 2, C. 100')
jawaban = str(input('Masukan Jawaban\t: '))
if jawaban == ('A') or ('a'):
    print('Jawabanmu Benar!')
else:
    print('Jawabanmu Salah')