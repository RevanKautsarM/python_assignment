# Dibuat Oleh   : Revan Kautsar Mulyana
# Tanggal       : 22-10-2024
# PROJECT 100
number1 = input('Masukan Angka Ke Satu\t: ')
num1 = int(number1)
sign = input('+-*/\t: ')
number2 = input('Masukan Angka Ke Dua\t: ')
num2 = int(number2)

if sign == '+':
    print('Jumlah Pertambahan\t= ' +str(num1 + num2))
elif sign == '-':
    print('Jumlah Pengurangan\t= ' +str(num1 - num2))
elif sign == '*':
    print('Jumlah Perkalian\t= ' +str(num1 * num2))
elif sign == '/':
    print('Jumlah Pembagian\t= ' +str(num1 / num2))
else:
    print('Masukan + , - ,* ,/')