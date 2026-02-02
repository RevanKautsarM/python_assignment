berat = float(input("Berat badan (kg): "))
tinggi = float(input("Tinggi badan (m): "))

bmi = berat / (tinggi ** 2)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Kurus")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Gemuk")
else:
    print("Obesitas")