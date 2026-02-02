import random

pilihan = ["gunting", "batu", "kertas"]
komputer = random.choice(pilihan)

user = input("Pilih (gunting/batu/kertas): ")

if user == komputer:
    print("Seri")
elif (user == "gunting" and komputer == "kertas") or \
     (user == "batu" and komputer == "gunting") or \
     (user == "kertas" and komputer == "batu"):
    print("Menang")
else:
    print("Kalah")

print("Komputer:", komputer)