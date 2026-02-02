nama = input("Nama: ")
pesan = input("Pesan: ")

with open("buku_tamu.txt", "a") as f:
    f.write(f"{nama} - {pesan}\n")

print("Data tersimpan.")