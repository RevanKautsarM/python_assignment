kata = input("Kata yang dicari: ")

with open("data.txt") as f:
    isi = f.read()

if kata in isi:
    print("Kata ditemukan.")
else:
    print("Kata tidak ditemukan.")
