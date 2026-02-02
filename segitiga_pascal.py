n = int(input("Jumlah baris: "))

for i in range(n):
    angka = 1
    for j in range(i + 1):
        print(angka, end=" ")
        angka = angka * (i - j) // (j + 1)
    print()
