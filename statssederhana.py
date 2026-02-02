data = list(map(int, input("Masukkan angka (pisah spasi): ").split()))

rata = sum(data) / len(data)
data.sort()
median = data[len(data)//2]

print("Rata-rata:", rata)
print("Median:", median)
