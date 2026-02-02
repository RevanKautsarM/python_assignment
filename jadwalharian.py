jadwal = []

while True:
    kegiatan = input("Kegiatan (stop untuk selesai): ")
    if kegiatan == "stop":
        break
    jadwal.append(kegiatan)

print("Jadwal hari ini:")
for j in jadwal:
    print("-", j)