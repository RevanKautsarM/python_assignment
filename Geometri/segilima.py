# Dibuat Oleh : Revan
# Tanggal     : 24-9-2024
# Soal Segilima/PROJECT100

print('='*40)
print('           PROGRAM SEGI LIMA          ')
print('='*40)

def segilima(): 
 ka = int(input('Masukan Keliling Alas: '))
 la = int(input('Masukan Luas Alas: '))
 tp = int(input('Masukan Tinggi Prisma: '))

 lp = 2 * la + ka * tp

 print('Luas permukaan segi lima adalah :', lp , 'cm2')