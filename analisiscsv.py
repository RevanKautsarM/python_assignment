# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100
import csv
with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
