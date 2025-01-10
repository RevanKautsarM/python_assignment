# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100
import random

def batu_kertas_gunting():
    choices = ["batu", "kertas", "gunting"]
    user_choice = input("Pilih batu, kertas, atau gunting: ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "batu" and computer_choice == "gunting") or \
         (user_choice == "kertas" and computer_choice == "batu") or \
         (user_choice == "gunting" and computer_choice == "kertas"):
        print("Kamu Menang!")
    else:
        print("Kamu Kalah!")

batu_kertas_gunting()