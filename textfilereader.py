# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100

def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read())

read_file("example.txt")