print('====================================')
print('         PROGRAM SEGITIGA           ')
print('====================================')

a = int(input('Masukan Alas Segitiga: '))
t = int(input('Masukan Tinggi Segitiga: '))

ab = int(input('Masukan AB Segitiga: '))
bc = int(input('Masukan BC Segitiga: '))
ca = int(input('Masukan CA Segitiga: '))

luas = 1/2 * a * t
k = ab + bc + ca

print('Luas Segitiga Adalah', luas ,'cm2')
print('Keliling Segitiga Adalah', k ,'cm2')
