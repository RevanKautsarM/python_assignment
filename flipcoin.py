import random
print('!!!\t\t FLIP COIN GAME \t\t!!!')

choice=input('Tebak Koin\t:')

num=random.randint(1, 2)

if num==1:
    result='Gambar'

elif num==2:
    result='Angka'

if choice==result:
    print('Selamat Tebakkan mu Benar!! :D')

else:
    print('Yahh Tebakan mu Salah, Silahkan Coba Lagi Nanti :D')

