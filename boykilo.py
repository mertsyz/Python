print("""*********
Beden Kitle İndeksi Hesapla
*********""")

kilo = int(input("Kilonuzu Girin: "))
boy = float(input("Boyunuzu Girin: "))
hesap = (kilo / (boy ** 2))

if (hesap < 18.5):
    print("Beden Kitle İndeksi: {} - Zayıf".format(hesap))
elif (hesap > 18.5 and hesap < 25):
    print("Beden Kitle İndeksi: {} - Normal".format(hesap))
elif (hesap > 25 and hesap < 30):
    print("Beden Kitle İndeksi: {} - Fazla Kilolu".format(hesap))
elif (hesap > 30):
    print("Beden Kitle İndeksi: {} - Obez".format(hesap))
else:
    print("Hata!")
