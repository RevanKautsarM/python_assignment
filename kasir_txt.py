total = 0

while True:
    nama = input("Nama barang (ketik 'stop' untuk selesai): ")
    if nama == "stop":
        break
    harga = int(input("Harga: "))
    total += harga

with open("struk.txt", "w") as f:
    f.write(f"Total belanja: {total}")

print("Struk dibuat.")
