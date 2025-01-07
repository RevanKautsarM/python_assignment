# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100

n = int(input("Masukkan bilangan: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Bukan bilangan prima.")
            break
    else:
        print("Bilangan prima.")
else:
    print("Bukan bilangan prima.")
