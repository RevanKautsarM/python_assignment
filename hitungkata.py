antrian = []

while True:
    print("1. Tambah  2. Panggil  3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama: ")
        antrian.append(nama)
    elif pilih == "2":
        if antrian:
            print("Dipanggil:", antrian.pop(0))
        else:
            print("Antrian kosong")
    elif pilih == "3":
        break