a = int(input("Angka 1: "))
b = int(input("Angka 2: "))

x, y = a, b
while y:
    x, y = y, x % y

fpb = x
kpk = a * b // fpb

print("FPB:", fpb)
print("KPK:", kpk)
