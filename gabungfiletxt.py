with open("file1.txt") as f1, open("file2.txt") as f2:
    isi = f1.read() + "\n" + f2.read()

with open("gabungan.txt", "w") as f:
    f.write(isi)

print("File digabung.")
