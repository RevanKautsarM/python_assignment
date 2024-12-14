def jumlah_kalori():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
    umur = int(input("Masukkan umur: "))
    kalori = 66 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * umur)
    print(f"Jumlah kalori: {kalori}")

jumlah_kalori()