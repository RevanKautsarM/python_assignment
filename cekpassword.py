pw = input("Password: ")

if len(pw) >= 8 and any(c.isdigit() for c in pw):
    print("Password kuat")
else:
    print("Password lemah")