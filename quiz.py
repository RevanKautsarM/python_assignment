# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100

def quiz():
    score = 0
    answer = input("Apa kepanjangan dari HTML?: ")
    if answer.lower() == "Hypertext Markup Language" or "hypertext markup language":
        score += 1
    print(f"Your score: {score}")

quiz()
