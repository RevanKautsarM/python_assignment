# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100
n = int(input("Masukkan tinggi piramida: "))
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(map(str, range(1, i + 1))))
