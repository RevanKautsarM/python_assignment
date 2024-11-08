# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 8-11-2024
# PROJECT100

harga_barang = int(input('Masukan harga barang :'))
diskon = 12.5/100

if int(harga_barang) >= 100000:
    hitung = harga_barang*diskon
    print(hitung)
elif int(harga_barang) >= 50:
    print('Barang tidak dijual10')
elif int(harga_barang) <= 10:
    print('Barang harus di restock')


else:
    print('Barang tidak mendapatkan diskon')