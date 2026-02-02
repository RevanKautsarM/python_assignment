import random

jumlah = int(input("Jumlah lemparan: "))

for i in range(jumlah):
    print(random.randint(1, 6))