nilai = []
jml = int(input('Jumlah Yang Akan Di Input\t:'))

for i in range(jml):
    nilai.append(float(input(f'Nilai Ke {i+1}\t:')))

total = rata2 = max = min = 0
for data in nilai:
    total += data
    if data > max:
        max = data

    min = data
    if data < min:
        min = data

print(total)
print(f'Rata-rata\t:{total/jml}')
print(f'Nilai Terbesar\t:{max}')
print(f'Nilai Terkecil\t:{min}')