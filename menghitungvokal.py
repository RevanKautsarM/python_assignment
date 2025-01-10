# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("Masukan kata disini!"))