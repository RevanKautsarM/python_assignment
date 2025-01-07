# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100

n = int(input("Masukkan batas angka: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
