teks = input("Teks: ").lower()
vokal = "aiueo"

jml_vokal = 0
jml_konsonan = 0

for c in teks:
    if c.isalpha():
        if c in vokal:
            jml_vokal += 1
        else:
            jml_konsonan += 1

print("Vokal:", jml_vokal)
print("Konsonan:", jml_konsonan)
