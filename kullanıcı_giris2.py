print("""**************
Kullanıcı Girişi Programı
**************""")

sys_kullanıcı = "mert123"
sys_parola = "mert321"
giris_hakki = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    kullanıcı_parola = input("Parola: ")
    if (kullanıcı_adı != sys_kullanıcı and kullanıcı_parola == sys_parola):
        print("Kullanıcı Adı Hatalı!!!")
        giris_hakki -= 1
        print("Kalan Giriş Hakkı:",giris_hakki)
    elif (kullanıcı_adı == sys_kullanıcı and kullanıcı_parola != sys_parola):
        print("Parola Hatalı!!!")
        giris_hakki -= 1
        print("Kalan Giriş Hakkı:",giris_hakki)
    elif (kullanıcı_adı != sys_kullanıcı and kullanıcı_parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı!!!")
        giris_hakki -= 1
        print("Kalan Giriş Hakkı:",giris_hakki)
    else:
        print("Sisteme Giriş Yapıldı")
        break
    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitti...")
        break
