# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100
import random
import string

def password_generator():
    panjang = int(input("Masukkan panjang password: "))
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for i in range(panjang))
    print("Password Anda: ", password)

password_generator()