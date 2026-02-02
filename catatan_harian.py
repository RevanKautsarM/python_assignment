catatan = input("Tulis catatan hari ini: ")

with open("catatan.txt", "a") as f:
    f.write(catatan + "\n")

print("Catatan disimpan.")