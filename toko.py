# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

print('\033[1m==========SELAMAT DATANG DI TOKO ALAT TULIS==========')
harga_buku = 5000
harga_penghapus = 1000
harga_pulpen = 3000
harga_pensil = 2000
harga_penggaris = 3000
harga_penserut = 4000
harga_spidol = 2000

buku = int(input('Ingin Membeli Berapa Buku?: '))
penghapus = int(input('Ingin Membeli Berapa Penghapus?: '))
pulpen = int(input('Ingin Membeli Berapa Pulpen?: '))
pensil = int(input('Ingin Membeli Berapa Pensil?: '))
penggaris = int(input('Ingin Membeli Berapa Penggaris?: '))
penserut = int(input('Ingin Membeli Berapa Penserut?: '))
spidol = int(input('Ingin Membeli Berapa Spidol?: '))

jml_buku = harga_buku*buku
jml_penggaris = harga_penggaris*penggaris
jml_penghapus = harga_penghapus*penghapus
jml_pulpen = harga_pulpen*pulpen
jml_pensil = harga_pensil*pensil
jml_penserut = harga_penserut*penserut
jml_spidol = harga_spidol*spidol
total = jml_buku+jml_penggaris+jml_penghapus+jml_penserut+jml_pensil+jml_pulpen+jml_spidol

diskon = total*12.5/100
jumlah = total-diskon

print('\033[95mJumlah: ', total)
print('Diskon: ', diskon)
print('Harus Bayar: \033[1m', jumlah)