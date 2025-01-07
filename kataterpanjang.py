# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100

text = input("Masukkan sebuah string: ")
words = text.split()
longest_word = max(words, key=len)
print("Kata terpanjang adalah:", longest_word)
print("Dengan panjang:", len(longest_word))
