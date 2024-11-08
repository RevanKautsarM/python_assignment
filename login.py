# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

USERNAME = 'MionAlbeiro'
PASSWORD = 'HUSMLM'

username = input('Masukan Username\t: ')
password = input('Masukan Password\t: ')

if username != USERNAME:
    print('Username tidak tersedia')
elif password != PASSWORD:
    print('Password salah')
else:
    print('Selamat Datang',username)