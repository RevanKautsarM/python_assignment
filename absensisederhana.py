nama = input("Nama: ")
hadir = input("Hadir? (y/n): ")

with open("absensi.txt", "a") as f:
    f.write(f"{nama} - {hadir}\n")

print("Absensi dicatat.")