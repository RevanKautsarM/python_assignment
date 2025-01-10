# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100
def shorten_url(url):
    return f"http://short.url/{hash(url)}"

print(shorten_url("https://www.contoh.com"))