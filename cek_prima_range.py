awal = int(input("Awal: "))
akhir = int(input("Akhir: "))

for n in range(awal, akhir + 1):
    if n > 1:
        prima = True
        for i in range(2, n):
            if n % i == 0:
                prima = False
                break
        if prima:
            print(n)