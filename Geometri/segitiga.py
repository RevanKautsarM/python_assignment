# Dibuat Oleh : Revan
# Tanggal     : 24-9-2024
# Soal Segitiga/PROJECT100

print('====================================')
print('         PROGRAM SEGITIGA           ')
print('====================================')
def segitiga():
 a = int(input('Masukan Alas Segitiga: '))
 t = int(input('Masukan Tinggi Segitiga: '))

 ab = int(input('Masukan AB Segitiga: '))
 bc = int(input('Masukan BC Segitiga: '))
 ca = int(input('Masukan CA Segitiga: '))

 luas = 1/2 * a * t
 k = ab + bc + ca

print('Luas Segitiga Adalah', luas ,'cm2')
print('Keliling Segitiga Adalah', k ,'cm2')
