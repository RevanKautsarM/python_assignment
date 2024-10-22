# Dibuat Oleh : Revan
# Tanggal     : 24-9-2024
# Soal Persegi/PROJECT100

print('='*40)
print('             PROGRAM PERSEGI           ')
print('='*40)
def persegi():
 s = int(input('Masukan Sisi Persegi: '))

 l = lambda s: s * s
 k = lambda s: 4 * s
 print('Volume Persegi Adalah: ',l(s) ,'cm')
 print('Luas Persegi Adalah: ',k(s) ,'cm')