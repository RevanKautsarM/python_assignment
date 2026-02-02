saldo = 0

while True:
    print("1. Tambah 2. Kurang 3. Keluar")
    p = input("Pilih: ")

    if p == "1":
        saldo += int(input("Jumlah: "))
    elif p == "2":
        saldo -= int(input("Jumlah: "))
    elif p == "3":
        break

print("Saldo akhir:", saldo)