import random

a = random.randint(1, 10)
b = random.randint(1, 10)

jawab = int(input(f"{a} + {b} = "))

if jawab == a + b:
    print("Benar")
else:
    print("Salah")