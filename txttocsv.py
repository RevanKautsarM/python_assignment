import csv

with open("data.txt") as txt, open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for baris in txt:
        writer.writerow([baris.strip()])

print("Konversi selesai.")