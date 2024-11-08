# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

import os
os.system('cls')
print('='*40)
print('             PADAT,CAIR DAN GAS')
print('='*40)

suhu = int(input('Masukan Suhu\t: '))
if suhu <= 0:
    print('Padat')
elif 0 < suhu < 100:
    print('Cair')
else:
    print('Gas')