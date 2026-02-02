aktivitas = input("Aktivitas: ")

with open("log.txt", "a") as f:
    f.write(aktivitas + "\n")

print("Aktivitas dicatat.")