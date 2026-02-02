kalimat = input("Kalimat: ")
sensor = input("Kata disensor: ")

hasil = kalimat.replace(sensor, "*" * len(sensor))
print(hasil)