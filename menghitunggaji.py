def gaji_karyawan():
    nama = input("Masukkan nama: ")
    jam_kerja = float(input("Masukkan jam kerja: "))
    gaji_per_jam = float(input("Masukkan gaji per jam: "))
    gaji_total = jam_kerja * gaji_per_jam
    print(f"Gaji total {nama}: {gaji_total}")

gaji_karyawan()

