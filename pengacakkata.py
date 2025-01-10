# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100
word = input("Masukan kata: ")
shuffled = ''.join(random.sample(word, len(word)))
print("Kata yg diacak:", shuffled)